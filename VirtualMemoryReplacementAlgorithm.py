#Lanyechan 12-07-2023
def fifo(pages, frame_count=3):
    memory = []
    page_faults = 0
    steps = []

    for page in pages:
        if page not in memory:
            if len(memory) == frame_count:
                memory.pop(0)
            memory.append(page)
            page_faults += 1
            steps.append((memory.copy(), 'Fault'))
        else:
            steps.append((memory.copy(), 'Hit'))

    return page_faults, steps

def lru(pages, frame_count=3):
    memory = []
    page_faults = 0
    steps = []
    page_time = {}

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) == frame_count:
                lru_page = min(memory, key=lambda x: page_time[x])
                memory.remove(lru_page)
            memory.append(page)
            page_faults += 1
            steps.append((memory.copy(), 'Fault'))
        else:
            memory.remove(page)
            memory.append(page)
            steps.append((memory.copy(), 'Hit'))

        page_time[page] = i

    return page_faults, steps

def opt(pages, frame_count=3):
    memory = []
    page_faults = 0
    steps = []
    
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) == frame_count:
                # Find the page that will not be used for the longest time in the future
                future_uses = [pages[i+1:].index(m) if m in pages[i+1:] else float('inf') for m in memory]
                opt_page = memory[future_uses.index(max(future_uses))]
                memory.remove(opt_page)
            memory.append(page)
            page_faults += 1
            steps.append((memory.copy(), 'Fault'))
        else:
            steps.append((memory.copy(), 'Hit'))
            
    return page_faults, steps

# Example usage
page_sequence = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] #modify your p_sequence here
frame_count = 3  #modify your frame_count here

fifo_faults, fifo_steps = fifo(page_sequence, frame_count)
lru_faults, lru_steps = lru(page_sequence, frame_count)
opt_faults, opt_steps = opt(page_sequence, frame_count)

# Print the results
print("FIFO Algorithm:")
print(f"Total Page Faults: {fifo_faults}")
for step, status in fifo_steps:
    print(f"Memory: {step}, Status: {status}")
    
print("\nLRU Algorithm:")
print(f"Total Page Faults: {lru_faults}")
for step, status in lru_steps:
    print(f"Memory: {step}, Status: {status}")
    
print("\nOPT Algorithm:")
print(f"Total Page Faults: {opt_faults}")
for step, status in opt_steps:
    print(f"Memory: {step}, Status: {status}")