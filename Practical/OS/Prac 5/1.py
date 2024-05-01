process = list(input("Enter Processes").split())
arrival_time = list(map(float, input("Enter Arrival Times: ").split()))
burst_time = list(map(float, input("Enter Burst Time: ").split()))
finish_time = []
for i in range(len(burst_time)):
    temp = 0
    for j in range(0, i+1):
        temp = temp + burst_time[j]
    print(temp)
    finish_time.append(temp)


print(process)
print(arrival_time)
print(burst_time)
print(finish_time)
turnaround_time = [(finish_time[i] - arrival_time[i]) for i in range(len(finish_time))]
waiting_time = [(turnaround_time[i] - burst_time[i]) for i in range(len(turnaround_time))]

print(turnaround_time)
print(waiting_time)

def gantt_chart():
    maxfinish = max(finish_time)
    finish_time.insert(0, arrival_time[0])
    i = 0
    for processes, finish in zip(process, finish_time):
        barwidth = int((finish/maxfinish) * 50 + 10)
        print(f"| {processes}", end=" ")
        print(" " * barwidth, end="")
        print(f" ({finish_time[i]} - {finish_time[i+1]})", end = "")
        i += 1
    print("|")

gantt_chart()