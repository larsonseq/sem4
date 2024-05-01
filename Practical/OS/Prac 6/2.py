process = list(input("Enter Processes: ").split())
arrivalTime = list(map(float, input("Enter arrival time: ").split()))
burstTime = list(map(float, input("Enter Burst time: ").split()))
quantum = int(input("Enter time quantum: "))
finishtime = [0] * len(process)
z = tuple(zip(process, arrivalTime, burstTime, burstTime, [0]*len(process)))

print(z)

p = []
for i in z:
    p.append(list(i))
print(p)
totalcount = 0
for i in burstTime:
    totalcount += i

totaltime = arrivalTime[0]

while not totalcount <= 0:
    for i in range(len(process)):
        if p[i][4] != 0:
            continue
        if p[i][3] <= quantum:
            totaltime = totaltime + p[i][3]
            totalcount = totalcount - p[i][3]
            p[i][3] = 0
            p[i][4] = 1
            finishtime[i] = totaltime
        if p[i][3] > quantum:
            totalcount = totalcount - quantum
            totaltime = totaltime + quantum
            p[i][3] = p[i][3] - quantum

turnaround = [(finishtime[i] - arrivalTime[i]) for i in range(len(process))]
waiting = [(turnaround[i] - burstTime[i]) for i in range(len(process))]

print(finishtime)
print(turnaround)
print(waiting)