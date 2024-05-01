process = input("Enter processes: ").split()
arrival_time = list(map(int, input("Enter arrival time: ").split()))
burst_time = list(map(int, input("Enter burst time: ").split()))
quantum = int(input("Enter time quantum: "))
p = []
gantt = ["|"]
z = tuple(zip(process.copy(), arrival_time.copy(), burst_time.copy(), burst_time.copy(), [0]*len(process)))
for i in z:
    print(i)

for i in z:
    p.append(list(i))
# print(p)

finishtime = [0] * len(process)

total_time = 0
totalcount = arrival_time[0]
for i in burst_time:
    totalcount += i

TempForGantt = totalcount
print(totalcount)
print(len(process))
while not totalcount <= 0:
    for i in range(len(process)):
        if p[i][4] != 0:
            continue 
        if p[i][3] <= quantum and p[i][3]>=0:
            barwidth = " " * int(p[i][3] * 40 / TempForGantt)
            TempForGantt2 = total_time
            totalcount = totalcount - p[i][3]
            total_time = total_time + p[i][3]
            p[i][3] = 0
            finishtime[i] = total_time
            p[i][4] = 1
            # print("I was here 1")
            gantt.append(f" {p[i][0]} {barwidth} {TempForGantt2}-{total_time}|")
        
        elif p[i][3] > quantum:
            TempForGantt2 = total_time
            barwidth = " " * int(quantum * 40 / TempForGantt)
            totalcount = totalcount - quantum
            total_time = total_time + quantum
            p[i][3] = p[i][3] - quantum
            # print("I was here 2") 
            gantt.append(f" {p[i][0]} {barwidth} {TempForGantt2}-{total_time}|")

print(finishtime)

turnaroundtime = [(finishtime[i] - p[i][1]) for i in range(len(process))]
waitingtime = [(turnaroundtime[i] - p[i][2]) for i in range(len(process))]

print(turnaroundtime)
print(waitingtime)

x = "\n".join(gantt)
print(x)