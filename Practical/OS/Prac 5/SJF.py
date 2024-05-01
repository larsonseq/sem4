n = int(input("Enter Number of Processes: "))
processes = []
burst_time = []
arrival_time = []
waiting_time = []
finish_time = []
turnaround_time = []

for i in range(0, n):
   processes.append(input("Enter process Name: "))
   burst_time.append(float(input(f"Enter burst time of {processes[i]}:")))
   arrival_time.append(float(input(f"Enter arrival time of {processes[i]}:")))
   print("\n")


# Keep the first process fixed
first_process = processes[0]
first_burst_time = burst_time[0]
first_arrival_time = arrival_time[0]


# Sort remaining processes based on burst time
remaining_processes = processes[1:]
remaining_burst_time = burst_time[1:]
remaining_arrival_time = arrival_time[1:]


# Sort remaining processes based on burst time and arrival time
process_data = sorted(zip(remaining_processes, remaining_burst_time, remaining_arrival_time),
                     key=lambda x: (x[1], x[2]))


sorted_processes, sorted_burst_time, sorted_arrival_time = zip(*process_data)


# Include the first process in the sorted data
sorted_processes = (first_process,) + sorted_processes
sorted_burst_time = (first_burst_time,) + sorted_burst_time
sorted_arrival_time = (first_arrival_time,) + sorted_arrival_time


finish_time.append(sorted_burst_time[0])
for i in range(1, n):
   finish_time.append(finish_time[i - 1] + sorted_burst_time[i])


for i in range(0, n):
   turnaround_time.append(finish_time[i] - sorted_arrival_time[i]) 


average_turnaround_time = sum(turnaround_time) / n


for i in range(0, n):
   waiting_time.append(turnaround_time[i] - sorted_burst_time[i])


average_waiting_time = sum(waiting_time) / n


print("\n{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Process", 'Arrival', 'Burst', 'Finish', 'Turnaround', 'Waiting'))
for i in range(0, n):
   print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
       str(sorted_processes[i]), str(sorted_arrival_time[i]), str(sorted_burst_time[i]),
       str(finish_time[i]), str(turnaround_time[i]), str(waiting_time[i])
   ))


print(f"\nAverage Turnaround Time: {average_turnaround_time}\nAverage Waiting Time: {average_waiting_time}")




def draw_gantt_chart(processes, finish_times):
   chart = []

   # Total finish time for scaling
   total_finish_time = max(finish_times)

   # Displaying Gantt chart
   print("\nGantt Chart\n")

   for process, finish_time in zip(processes, finish_times):
       bar_width = int((finish_time / total_finish_time) * 20)  # Adjust width based on total finish time
       print(f"| {process} ", end="")
       print(" " * bar_width, end="")
       print(f" ({finish_time})", end=" ")
       chart.append((process, finish_time))

   # Displaying process names and finish times
   print("\nProcess Finish Times:")
   for process, finish_time in chart:
       print(f"{process}: {finish_time}")

draw_gantt_chart(sorted_processes, finish_time)
