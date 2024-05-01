n = int(input("Enter Number of Processes: "))
processes = []
burst_time =[]
arrival_time = []
#start_time = []
waiting_time = []
finish_time = []
turnaround_time = []


for i in range(0,n):
   processes.append(input("Enter process Name: "))
   burst_time.append(float(input(f"Enter burst time of {processes[i]}:")))
   arrival_time.append(float(input(f"Enter arrival time of {processes[i]}:")))
   print("\n")


finish_time.append(burst_time[0])
for i in range(1, n):
   finish_time.append(finish_time[i-1] + burst_time[i])


for i in range(0, n):
   turnaround_time.append(finish_time[i] - arrival_time[i])




average_turnaround_time = 0
for i in range(0, n):
   average_turnaround_time += (turnaround_time[i] / n)


for i in range(0, n):
   waiting_time.append(turnaround_time[i] - burst_time[i])


average_waiting_time = 0
for i in range(0, n):
   average_waiting_time += (waiting_time[i] / n)


average_turnaround_time = 0
for i in range(0, n):
   average_turnaround_time += (turnaround_time[i] / n)


print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Process", 'Arrival','Burst', 'Finish', 'Turnaround', 'waiting'))
for i in range(0, n):
   print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(str(processes[i]), str(arrival_time[i]), str(burst_time[i]),str(finish_time[i]), str(turnaround_time[i]), str(waiting_time[i])))
print(f"average turnaround time: {average_turnaround_time}\naverage waiting time: {average_waiting_time}")


print("Gantt Chart:")


def draw_gantt_chart(processes, finish_times):
   chart = []

   # Total finish time for scaling
   total_finish_time = max(finish_times)


   # Displaying Gantt chart
   print("\nGantt Chart:\n")
   print("-" * 40)


   for process, finish_time in zip(processes, finish_times):
       bar_width = int((finish_time / total_finish_time) * 40)  # Adjust width based on total finish time
       print(f"| {process} ", end="")
       print(" " * bar_width, end="")
       print(f" ({finish_time - burst_time[processes.index(process)]}-{finish_time})", end=" ")
       chart.append((process, finish_time))


   print("|\n" + "-" * 40)


   # Displaying process names and finish times
   print("\nProcess Finish Times:")
   for process, finish_time in chart:
       print(f"{process}: {finish_time}")


draw_gantt_chart(processes, finish_time)