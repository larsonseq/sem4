class BankerAlgorithm:
    def __init__(self, processes, resources, allocation, max_need, available):
        self.processes = processes
        self.resources = resources
        self.allocation = allocation
        self.max_need = max_need
        self.available = available
        self.need = []
        self.calculate_need()

    def calculate_need(self):
        self.need = []
        for i in range(len(self.processes)):
            need_row = [self.max_need[i][j] - self.allocation[i][j] for j in range(len(self.resources))]
            self.need.append(need_row)

    def is_safe_state(self):
        work = self.available.copy()
        finish = [False] * len(self.processes)
        safe_sequence = []
        while True:
            found = False
            for i in range(len(self.processes)):
                if not finish[i] and all(need <= work[j] for j, need in enumerate(self.need[i])):
                    work = [work[j] + self.allocation[i][j] for j in range(len(self.resources))]
                    safe_sequence.append(self.processes[i])
                    finish[i] = True
                    found = True
            if not found:
                break
        return all(finish), safe_sequence

def take_user_input():
    processes = int(input("Enter the number of processes: "))
    resources = int(input("Enter the number of resources: "))
    allocation = []
    max_need = []
    available = []

    print("Enter allocation matrix:")
    for i in range(processes):
        allocation.append(list(map(int, input().split())))
    print("Enter max need matrix:")
    for i in range(processes):
        max_need.append(list(map(int, input().split())))
    print("Enter available resources:")
    available = list(map(int, input().split()))

    return processes, resources, allocation, max_need, available

if __name__ == "__main__":
    processes, resources, allocation, max_need, available = take_user_input()

    banker = BankerAlgorithm(list(range(processes)), list(range(resources)), allocation, max_need, available)

    safe, sequence = banker.is_safe_state()

    if safe:
        print("Safe state")
        print("Safe sequence:", sequence)
        total_resources = [sum(col) for col in zip(*max_need)]
        print("Total resources:", total_resources)
        print("Need Matrix:")
        for row in banker.need:
            print(row)
    else:
        print("Unsafe state")
