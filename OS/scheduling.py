


class Process:
    def __init__(self, arrival, burst, id):
        self.arrival = arrival
        self.burst = burst
        self.id = id
        self.remaining = burst
        self.start_time = 0
        self.end_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def FCFS(processes):
    processes.sort(key=lambda x: x.arrival)
    processes[0].start_time = processes[0].arrival
    processes[0].end_time = processes[0].burst + processes[0].start_time
    processes[0].waiting_time = processes[0].start_time - processes[0].arrival
    processes[0].turnaround_time = processes[0].end_time - processes[0].arrival
    for i in range(1, len(processes)):
        processes[i].start_time = processes[i-1].end_time
        processes[i].end_time = processes[i].burst + processes[i].start_time
        processes[i].waiting_time = processes[i].start_time - processes[i].arrival
        if processes[i].waiting_time < 0:
            processes[i].waiting_time = 0
        processes[i].turnaround_time = processes[i].end_time - processes[i].arrival
    return processes

def SJF(processes):
   #TODO: Implement SJF
   True

def pp(processes: list[Process]) -> None:
    print("processes", [x.id for x in processes])
    print("end_time", [x.end_time for x in processes])
    print("average waiting time: ", sum(x.waiting_time for x in processes)/len(processes))


if __name__ == "__main__":
    execution_list = [Process(0, 4, 1), Process(2, 12, 2), Process(5, 2, 3), Process(6, 6, 4), Process(8, 10, 5), Process(12, 3, 6), Process(15, 8, 7), Process(22, 5, 8)]
    print("Before:")
    pp(execution_list)
    list = FCFS(execution_list)
    print("After:")
    pp(list)