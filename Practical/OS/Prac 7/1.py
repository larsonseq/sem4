class Bankers():
    def __init__(self, process, resource, allocation, maxneed, available):
        self.process = process
        self.resource = resource
        self.allocation = allocation
        self.maxneed = maxneed
        self.available = available
        self.need = self.calculate_need()

    def calculate_need(self):
        need = []
        for i in range(self.process):
            tempn = [self.maxneed[i][j] - self.allocation[i][j] for j in range(self.resource)]
            need.append(tempn)
        return need
    
    def is_safe(self):
        finish = [False] * self.process
        work = self.available.copy() 
        print(work)
        safeseq = []
        while True:
            found = False
            for i in range(self.process):
                if not finish[i] and all(need <= work[j] for j, need in enumerate(self.need[i])):
                    safeseq.append(i)
                    work = [work[j] + self.allocation[i][j] for j in range(self.resource)]
                    finish[i] = True
                    found = True
                    self.totalres = work
            if not found:
                break
        return all(finish), safeseq

def take_input():
    np = int(input("Enter number of processes: "))
    resources = int(input("Enter number of processes: "))
    allocation = []
    maxneed = [] 
    for i in range(np):
        allocation.append(list(map(int, input(f"Enter allocation for process {i+1}: ").split())))
    
    for i in range(np):
        maxneed.append(list(map(int, input(f"Enter max for process {i+1}: ").split())))
    
    available = (list(map(int, input("Enter available resources: ").split())))

    return np, resources, allocation, maxneed, available

process, res, alloc, mneed, avail = take_input()

bank = Bankers(process, res, alloc, mneed, avail)
issafe, seq = bank.is_safe()
if issafe:
    print("Safe State")
    print(f"Safe sequence: {[f'P{i}' for i in seq]}")
    totalres = bank.totalres
    print(f"Total resource: {totalres}")
    print("Need matrix:")
    for i in bank.need:
        print(i)
else:
    print("System is not insafe sequence:")