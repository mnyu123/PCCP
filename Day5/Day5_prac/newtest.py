class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = processes[i - 1].burst_time + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = processes[i].burst_time + waiting_time[i]

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i].pid}\t\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

def solution(processes):
    answer = []
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6),
        Process(5, 4, 2)
    ]

    fcfs(processes)

    # Calculate waiting time sum based on process priority
    waiting_time_sum = [0] * 10
    for process in processes:
        waiting_time_sum[process.pid - 1] += process.burst_time

    answer.append(sum(waiting_time_sum))
    answer.extend(waiting_time_sum)

    return answer

answer = solution(processes)
print(answer)  # Print the answer array
