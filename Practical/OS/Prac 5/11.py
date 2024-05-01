process = input("Enter Processes: ").split()
arrival_time = list(map(float, input("Enter arrival time: ").split()))
burst_time = list(map(float, input("Enter Burst Time: ").split()))
finish_time = []
for i in range(len(burst_time)):
    temp = 0
    for j in range(0, i+1):
        temp = temp + burst_time[j]
    finish_time.append(temp)

turnaround_time = [(finish_time[i] - arrival_time[i]) for i in range(len(burst_time))]
waiting_time = [(turnaround_time[i] - burst_time[i]) for i in range(len(turnaround_time))]

print(process)
print(arrival_time)
print(burst_time)
print(finish_time)
print(turnaround_time)
print(waiting_time)

def gantt_chart():
    maxTime = max(finish_time)
    temp = finish_time.copy()
    temp.insert(0, arrival_time[0]) 
    i = 0
    for p, f in zip(process, finish_time):
        barwidth = int(((temp[i+1] - temp[i]) / maxTime) * 40 + 10)
        print("f" * barwidth)
        print(f"| {p} ", end = "")
        print(" " * barwidth, end = "")
        print(f" ({temp[i]} - {temp[i+1]})", end = "")
        i = i+1
    print("|")

gantt_chart()