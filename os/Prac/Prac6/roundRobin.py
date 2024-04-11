if __name__ == '__main__': 
    print("Enter Total Process Number: ")
    total_p_no = int(input())
    total_time = 0
    total_time_counted = 0 
    proc = []
    wait_time = 0
    turnaround_time = [0] * total_p_no
    gantt_chart = []

    for _ in range(total_p_no): 
        print("Enter process arrival time and burst time")
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1] 
        proc.append([arrival, burst, remaining_time, 0]) 
        total_time += burst

    print("Enter time quantum")
    time_quantum = int(input())
 
    while total_time != 0: 
        for i in range(len(proc)): 
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2] 
                proc[i][2] = 0
                gantt_chart.append((i, total_time_counted))
            elif proc[i][2] > 0: 
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
                gantt_chart.append((i, total_time_counted))

            if proc[i][2] == 0 and proc[i][3] != 1:  
                wait_time += total_time_counted - proc[i][0] - proc[i][1]
                turnaround_time[i] = total_time_counted - proc[i][0] 
                proc[i][3] = 1
 
    print("{:<10} {:<10} {:<10} {:<10}".format("Process", 'Arrival', 'Burst', 'Turnaround'))
    for i in range(total_p_no):
        print("{:<10} {:<10} {:<10} {:<10}".format(
            str(i), str(proc[i][0]), str(proc[i][1]), str(turnaround_time[i])))
    print("\nAvg Waiting Time is ", (wait_time * 1) / total_p_no)
    print("Avg Turnaround Time is ", (sum(turnaround_time) * 1) / total_p_no)
 
    print("\nGantt Chart:")
    print("-" * 40)
    for i, finish_time in gantt_chart:
        print(f"| P{i} ", end="")
        print(" " * 3, end="")
    print("|\n" + "-" * 40)
