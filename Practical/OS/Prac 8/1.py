def first_fit(process, block):
    allocation = [-1] * (len(process) + 1)
    for i in range(1, len(process) + 1):
        for j in range(1, len(block)):
            if block[j] >= process[i]:
                allocation[i] = j
                block[j] = block[j] - process[i]
                break
    print(allocation)
    return allocation


def best_fit(process, block):
    print(block)
    allocation = [-1] * (len(process) + 1)
    for i in range(1, len(process) + 1):
        best = -1
        for j in range(1, len(block)):
            print(j)
            if block[j] >= process[i]:
                if best == -1 or block[j] < block[best]:
                    best = j
        if not best == -1:
            allocation[i] = best
            block[best] = block[best] - process[i]
    return allocation


def worst_fit(process, block):
    allocation = [-1] * (len(process) + 1)
    for i in range(1, len(process) + 1):
        worst = -1
        for j in range(1, len(block)):
            if block[j] >= process[i]:
                if worst == -1 or block[j] > block[worst]:
                    worst = j
        if not worst == -1:
            allocation[i] = worst
            block[worst] = block[worst] - process[i]
    return allocation


process = {}
psize = int(input("Enter number of processes: "))
for i in range(1,psize + 1):
    process[i] = int(input(f"Enter process {i}: "))

bsize = int(input("Enter block size: "))
block = [-1] * (bsize + 1)
for i in range(1, bsize + 1):
    block[i] = (int(input(f"Enter block {i}: ")))
print(block)

def print_allocation(allocation, process):
    print("Process No. Process size  Block Allocated")
    for i in range(1, len(process) + 1):
        if not allocation[i] == -1:
            print(f"{i}.\t{process[i]}\t {allocation[i]}")
        else:
            print(f"{i}.\t{process[i]}\t Not Allocated")

print("First Fit")
allocation = first_fit(process=process, block=block.copy())
print_allocation(allocation, process)

print("Best Fit")
allocation = best_fit(process=process, block=block.copy())
print_allocation(allocation, process)

print(f"Worst Fit")
allocation = worst_fit(process=process, block=block.copy())
print_allocation(allocation, process)
