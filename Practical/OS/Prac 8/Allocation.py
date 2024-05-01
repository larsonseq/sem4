def first_fit(processes, blocks):
    allocation = [-1] * (len(processes) + 1)
    for i in range(1, len(processes) + 1):
        for j in range(1, len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation

def best_fit(processes, blocks):
    allocation = [-1] * (len(processes) + 1)
    for i in range(1, len(processes) + 1):
        best_block = -1
        for j in range(1, len(blocks)):
            if blocks[j] >= processes[i]:
                if best_block == -1 or blocks[j] < blocks[best_block]:
                    best_block = j
        if best_block != -1:
            allocation[i] = best_block
            blocks[best_block] -= processes[i]
    return allocation

def worst_fit(processes, blocks):
    allocation = [-1] * (len(processes) + 1)
    for i in range(1, len(processes) + 1):
        worst_block = -1
        for j in range(1, len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_block == -1 or blocks[j] > blocks[worst_block]:
                    worst_block = j
        if worst_block != -1:
            allocation[i] = worst_block
            blocks[worst_block] -= processes[i]
    return allocation

def print_allocation_table(processes, allocation):
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(1, len(processes) + 1):
        print(f"{i}\t\t{processes[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i])
        else:
            print("Not Allocated")

# Taking input from user for processes
num_processes = int(input("Enter the number of processes: "))
processes = {}
for i in range(1, num_processes + 1):
    size = int(input(f"Enter size of process {i}: "))
    processes[i] = size

num_blocks = int(input("Enter the number of memory blocks: "))
blocks = {}
for i in range(1, num_blocks + 1):
    size = int(input(f"Enter size of block {i}: "))
    blocks[i] = size

print("\nFirst Fit Allocation:")
first_fit_allocation = first_fit(processes, blocks.copy())
print_allocation_table(processes, first_fit_allocation)

print("\nBest Fit Allocation:")
best_fit_allocation = best_fit(processes, blocks.copy())
print_allocation_table(processes, best_fit_allocation)

print("\nWorst Fit Allocation:")
worst_fit_allocation = worst_fit(processes, blocks.copy())
print_allocation_table(processes, worst_fit_allocation)
