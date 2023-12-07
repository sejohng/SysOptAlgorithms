# Name: Lanyechan
# VMAlgorithm
def fifo(pages, frame_count=4):
    memory = [None] * frame_count  # 
    page_faults = 0
    steps = []
    index_to_replace = 0  # Indicates the next position to replace
    
    for page in pages:
        if page not in memory:
            # Replace the page and only change the replaced position
            memory[index_to_replace] = page
            index_to_replace = (index_to_replace + 1) % frame_count  # Update replacement location
            page_faults += 1
            steps.append((memory.copy(), 'Fault'))
        else:
            # Page hits do not change anything in memory
            steps.append((memory.copy(), 'Hit'))
            
    return page_faults, steps


def lru(pages, frame_count=3):
    memory = [None] * frame_count  # init
    page_faults = 0
    steps = []
    page_time = {}  # Record the last time each page was visited
    
    for i, page in enumerate(pages):
        if page in memory:
            # Page hit, only update access time
            steps.append((memory.copy(), 'Hit'))
        else:
            # Page fault, need to replace
            if None in memory:
                # If there are still vacancies, fill the first vacancy
                replace_index = memory.index(None)
            else:
                # Find the least recently used page and replace it
                lru_page = min((page for page in memory if page is not None), key=page_time.get, default=None)
                replace_index = memory.index(lru_page)
            memory[replace_index] = page
            page_faults += 1
            steps.append((memory.copy(), 'Fault'))
            
        page_time[page] = i  # Update page last visited time
        
    return page_faults, steps

def opt(pages, frame_count=3):
    memory = [None] * frame_count  # init
    page_faults = 0
    steps = []
    
    for i, page in enumerate(pages):
        if page in memory:
            # page hit
            steps.append((memory.copy(), 'Hit'))
        else:
            # page fault
            if None in memory:
                # If there are still vacancies, fill the first vacancy
                replace_index = memory.index(None)
            else:
                # Find pages that will not be used for the longest time in the future and replace them
                future_uses = []
                for m in memory:
                    if m in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(m))
                    else:
                        future_uses.append(float('inf'))
                        
                # Select pages to replace based on future usage
                replace_index = future_uses.index(max(future_uses))
                
            memory[replace_index] = page
            page_faults += 1
            steps.append((memory.copy(), 'Fault'))
            
    return page_faults, steps

# Example usage
page_sequence = [1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6] #modify your p_sequence here
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