process = input("Enter process Names: ").split()
arrival_time = list(map(float, input("Enter arrival time: ").split()))
burst_time = list(map(float, input("Enter burst time: ").split()))

p = sorted(zip(process[1:], arrival_time[1:], burst_time[1:]), key = lambda x : (x[2], x[1]))
p.insert(0, (process[0], arrival_time[0], burst_time[0]))

finish_time = []
for i in range(len(p)):
    temp = 0
    for j in range(0, i+1):
        temp += p[j][2]
    finish_time.append(temp)

turnaround_time = [(finish_time[i] - p[i][1]) for i in range(len(finish_time))]

waiting_time = [(turnaround_time[i] - p[i][2]) for i in range(len(turnaround_time))]

for i in range(len(p)):
    print(p[i], end = "")
    print(f" {finish_time[i]} ", end = "")
    print(f" {turnaround_time[i]} ", end = "")
    print(f" {waiting_time[i]} ", end= "")
    print("")

def gantt_chart():
    maxtime = max(finish_time)
    tempfinish = finish_time.copy()
    tempfinish.insert(0, arrival_time[0])    
    for i in range(len(finish_time)):
        barwidth = int(((tempfinish[i+1] - tempfinish[i]) / maxtime) * 40 + 10)
        print("| ",p[i][0], end = "")
        print(" " * barwidth, end=" ")
        print(f" {tempfinish[i]} - {tempfinish[i+1]}", end = "")
    print("|")

gantt_chart()