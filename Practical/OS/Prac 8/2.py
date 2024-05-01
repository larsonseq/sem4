def first_fit(block, process):
    allocation = [-1] * (len(process) + 1)
    for i in range(1, len(process) + 1):
        for j in range(1, len(block)):
            if block[j] >= process[i]:
                allocation[i] = j
                block[j] -= process[i]
                break
    return allocation


def best_fit(block, process):
    allocation = [-1] * (len(process) + 1)
    for i in range(1, len(process) + 1):
        best = -1
        for j in range(1, len(block)):
            if block[j] >= process[i]:
                if best == -1 or block[best] > block[j]:
                    best = j
        if best != -1:
            allocation[i] = best
            block[best] -= process[i]
    return allocation


def worst_fit(block, process):
    allocation = [-1] * (len(process) + 1)
    for i in range(1, len(process) + 1):
        worst = -1
        for j in range(1, len(block)):
            if block[j] >= process[i]:
                if worst == -1 or block[j] > block[worst]:
                    worst = j
        if worst != -1:
            allocation[i] = worst
            block[worst] -= process[i]
    return allocation


def print_allocation(allocation, process):
    print(f"Process No Process Size Block Number")
    for i in range(1, len(process) + 1):
        if allocation[i] != -1:
            print(f"{i}.\t\t{process[i]}\t \t{allocation[i]}")
        else:
            print(f"{i}. \t\t{process[i]} \t\t Not Allocated")


psize = int(input("Enter Process size: "))
process = {}
for i in range(1, psize + 1):
    process[i] = int(input(f"Enter process {i}:"))

bsize = int(input("Enter No of blocks: "))
block = [-1] * (bsize + 1)
for i in range(1, bsize + 1):
    block[i] = int(input(f"Enter block {i}: "))

print("First Fit:")
allocation = first_fit(block.copy(), process)
print_allocation(allocation, process)

print("Best Fit:")
allocation = best_fit(block.copy(), process)
print_allocation(allocation, process)

print("Worst Fit:")
allocation = worst_fit(block.copy(), process)
print_allocation(allocation, process)