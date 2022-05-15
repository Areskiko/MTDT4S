



class Process:
    def __init__(self, arrival, burst, id):
        self.arrival = arrival
        self.burst = burst
        self.id = id
        self.remaining = burst
        self.start_time = 0
        self.end_time = 0
        self.optimal_end_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def FCFS(processes):
    """
    It sorts the processes by arrival time, then sets the start time of the first process to its arrival
    time, and the end time to its burst time plus its start time. Then, for each process after the
    first, it sets the start time to the end time of the previous process, and the end time to the burst
    time plus the start time. Then, it sets the waiting time to the start time minus the arrival time,
    and the turnaround time to the end time minus the arrival time

    :param processes: list of Process objects
    :return: A list of processes
    """
    processes.sort(key=lambda x: x.arrival)
    processes[0].start_time = processes[0].arrival
    processes[0].end_time = processes[0].burst + processes[0].start_time
    processes[0].optimal_end_time = 0
    processes[0].waiting_time = processes[0].start_time - processes[0].arrival
    processes[0].turnaround_time = processes[0].end_time - processes[0].arrival
    for i in range(1, len(processes)):
        processes[i].start_time = processes[i-1].end_time
        processes[i].end_time = processes[i].burst + processes[i].start_time
        processes[i].waiting_time = processes[i].start_time - \
            processes[i].arrival
        if processes[i].waiting_time < 0:
            processes[i].waiting_time = 0
        processes[i].turnaround_time = processes[i].end_time - \
            processes[i].arrival
        processes[i].optimal_end_time = processes[i].end_time - (processes[i].burst + processes[i].arrival)
    return processes


def list_swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]

def total_compute_time(processes: list[Process]) -> int:
    return sum(x.burst for x in processes)

def SJF(processes):
    """
    It takes a list of processes, sorts them by arrival time, then iterates through the list, finding
    the process with the shortest burst time that has arrived by the time the previous process has
    finished, and then sets the start time of the current process to the end time of the previous
    process, and the end time of the current process to the start time of the current process plus the
    burst time of the current process

    :param processes: a list of Process objects
    :return: A list of processes
    """
    processes[0].start_time = processes[0].arrival
    processes[0].end_time = processes[0].burst + processes[0].start_time
    processes[0].waiting_time = processes[0].start_time - processes[0].arrival
    processes[0].turnaround_time = processes[0].end_time - processes[0].arrival
    for i in range(1, len(processes)):
        possible_canditates = [x for x in processes[i:]
                               if x.arrival <= processes[i-1].end_time]
        possible_canditates.sort(key=lambda x: x.burst)
        list_swap(processes, i, processes.index(possible_canditates[0]))
        processes[i].start_time = processes[i-1].end_time
        processes[i].end_time = processes[i].burst + processes[i].start_time
        processes[i].waiting_time = processes[i].start_time - \
            processes[i].arrival
        if processes[i].waiting_time < 0:
            processes[i].waiting_time = 0
        processes[i].turnaround_time = processes[i].end_time - \
            processes[i].arrival
        processes[i].optimal_end_time = processes[i].end_time - (processes[i].burst + processes[i].arrival)
    return processes

def RR(processes: list[Process], quantum):
    result_list = []
    temp_queue = []
    done_list = []
    current: Process = None
    counter = 0
    for i in range(total_compute_time(processes)):
        a = True
        for process in processes:
            var1 = process.arrival <= i
            var2 = not (process in temp_queue or process in done_list)
            var3 = not process == current
            if var1 and var2 and var3:
                temp_queue.append(process)
        if current == None:
            current = temp_queue.pop(0)
        current.burst -= 1
        if current.burst == 0:
            current.end_time = i + 1
            result_list.append(current)
            done_list.append(current)
            counter = 0
            current = None
        else:
            if counter % quantum == 0 and counter != 0:
                result_list.append(current)
                temp_queue.append(current)
                current = temp_queue.pop(0)
            counter += 1
    return result_list


def SRTF(processes):
    result_list = []
    temp_queue = []
    done_list = []

def pp(processes: list[Process]) -> None:
    print("processes", [x.id for x in processes])
    print("end_time", [x.end_time for x in processes])
    print("optimal end time", [x.optimal_end_time for x in processes])
    print("difference", [x.end_time - x.optimal_end_time for x in processes])
    print("average waiting time: ", sum(
        x.optimal_end_time for x in processes)/len(processes))
    # print("Average turnaround time: ", sum(
        # x.turnaround_time for x in processes)/len(processes))


if __name__ == "__main__":
    execution_list = [Process(0, 4, 1), Process(2, 12, 2), Process(5, 2, 3), Process(
        6, 6, 4), Process(8, 10, 5), Process(12, 3, 6), Process(15, 8, 7), Process(22, 5, 8)]
    # list = FCFS(execution_list)
    # pp(list)
    # list2 = SJF(execution_list)
    # pp(list2)
    list = RR(execution_list, 6)
    pp(list)
