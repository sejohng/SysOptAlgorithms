# Name: Lanyechan
# DiskScheduleAlgorithm
def calculate_movement(sequence, current, direction, algorithm, max_disk_size=4999): #modify here
    movement = 0
    sequence = [current] + sequence  # Include the initial position
    order = []

    if algorithm == 'FCFS':
        order = sequence.copy()
        for request in sequence:
            movement += abs(current - request)
            current = request

    elif algorithm == 'SSTF':
        while sequence:
            closest = min(sequence, key=lambda x: abs(x - current))
            movement += abs(current - closest)
            current = closest
            order.append(closest)
            sequence.remove(closest)

    elif algorithm == 'SCAN':
            sequence.append(max_disk_size if direction == 'up' else 0)
            sequence.sort()
            idx = sequence.index(current)
            if direction == 'up':
                order = sequence[idx:] + sequence[:idx][::-1]
            else:
                order = sequence[:idx + 1][::-1] + sequence[idx + 1:]
            for i in range(len(order) - 1):
                movement += abs(order[i] - order[i + 1])
                
    elif algorithm == 'LOOK':
            sequence.sort()
            idx = sequence.index(current)
            if direction == 'up':
                order = sequence[idx:] + sequence[:idx][::-1]
            else:
                order = sequence[:idx + 1][::-1] + sequence[idx + 1:]
            for i in range(len(order) - 1):
                movement += abs(order[i] - order[i + 1])
                
    elif algorithm == 'C-SCAN':
        sequence.append(max_disk_size)
        sequence.append(0)
        sequence.sort()
        idx = sequence.index(current)
        
        # Modify the order to avoid duplicate max_disk_size and 0
        order = sequence[idx:]
        if max_disk_size not in order:
            order.append(max_disk_size)
        order += [0] + sequence[:idx]
        if 0 in sequence[:idx]:
            order.remove(0)
            
        # Keep the original movement calculation
        right_movement = max_disk_size - current  # Move from current to the rightmost end
        left_movement = sequence[idx - 1] if idx != 0 else 0  # Move from the leftmost end to the leftmost request
        return order, right_movement + left_movement
    
    elif algorithm == 'C-LOOK':
        sequence.sort()
        idx = sequence.index(current)
        
        # Determine the order of servicing the requests
        if direction == 'up':
            order = sequence[idx:] + sequence[:idx]
        else:
            order = sequence[:idx + 1][::-1] + sequence[idx + 1:][::-1]
            
        # Calculate the total movement
        right_movement = sequence[-1] - current  # Move from current to the rightmost request
        left_movement = 0
        if idx != 0:
            left_movement = sequence[idx - 1] - sequence[0]  # Move from the leftmost request to the rightmost request to the left of current
            
        movement = right_movement + left_movement
        
    return order, movement

#
requests = [86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130] #modify here
#requests = [98, 183, 37, 122, 14, 124, 65, 67]
current_position = 143 #modify here
previous_position = 125  #modify here
direction = 'up' if current_position > previous_position else 'down'

# define
algorithms = ['FCFS', 'SSTF', 'SCAN', 'LOOK', 'C-SCAN', 'C-LOOK']
results = {}

for algorithm in algorithms:
    order, movement = calculate_movement(requests.copy(), current_position, direction, algorithm)
    results[algorithm] = {'Order': order, 'Total Movement': movement}
    
# print
for alg, res in results.items():
    print(f"{alg} Order: {res['Order']}\nTotal Movement: {res['Total Movement']}")
    