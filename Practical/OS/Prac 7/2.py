class Bankers():
    def __init__(self,process, resource, allocation, maxneed, available):
        self.process = process
        self.resource = resource
        self.allocation = allocation
        self.maxneed = maxneed
        self.available = available
        self.need = self.createneed()
    
    def createneed(self):
        need = []
        for i in range(self.process):
            tempn = [self.maxneed[i][j] - self.allocation[i][j] for j in range(self.resource)]
            need.append(tempn)
        return need

    def issafe(self):
        work = self.available.copy()
        safeseq = []
        finish = [False] * self.process
        while True:
            found = False
            for i in range(self.process):
                if not finish[i] and all([need <= work[j] for j, need in enumerate(self.need[i])]):
                    safeseq.append(i)
                    finish[i] = True
                    found = True
                    work = [work[j] + alloc for j, alloc in enumerate(self.allocation[i])]
                    self.totalres = work
            if not found:
                break
        return all(finish), safeseq

def takeinput():
    process = int(input("Enter number of process: "))
    res = int(input("Enter number of resources: "))
    allocation = []
    for i in range(process):
        allocation.append(list(map(int, input(f"Enter allocation for process P{i+1}: ").split())))
    maxneed = []
    for i in range(process):
        maxneed.append(list(map(int, input(f"Enter max need for process P{i+1}: ").split())))
    available = list(map(int, input("Enter available resources: ").split()))
    return process, res, allocation, maxneed, available

p, r, a, mn, ava = takeinput()

bank = Bankers(p, r, a, mn, ava)
issafe, safeseq = bank.issafe()
if issafe:
    print("Is is a safe sequence")
    print(f"The safe sequence is {[f'P{i} ' for i in safeseq]}")
    print(f"Total resource is {bank.totalres}")
    print(f"Need matrix is:")
    for i in bank.need:
        print(i)
else:
    print("It is not safe")