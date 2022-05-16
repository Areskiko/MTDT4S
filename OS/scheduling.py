import copy


class Process:
    def __init__(self, arrival, burst, id, priority=0):
        self.arrival = arrival
        self.burst = burst
        self.id = id
        self.priority = priority
        self.remaining = burst
        self.optimal_end_time = arrival + burst
        self.start_time = 0
        self.end_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def FCFS(processes: list[Process]):
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
    return processes


def list_swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def total_compute_time(processes: list[Process]) -> int:
    return sum(x.burst for x in processes)


def SJF(processes: list[Process]):
    """
    It takes a list of processes, sorts them by arrival time, then iterates through the list, finding
    the process with the shortest burst time that has arrived by the time the previous process has
    finished, and then sets the start time of the current process to the end time of the previous
    process, and the end time of the current process to the start time of the current process plus the
    burst time of the current process

    :param processes: a list of Process objects
    :return: A list of processes
    """
    result_list = []
    arrived = []
    done_list = []
    current: Process = None
    counter = 0
    works = []
    arrival_time = 0
    while True:
        arrived.extend([x for x in processes if x.arrival <=
                       arrival_time and x not in done_list and x not in arrived])
        arrived.sort(key=lambda x: x.burst)
        current = arrived.pop(0)
        while current.burst != 0:
            current.burst -= 1
            arrival_time += 1
        current.end_time = arrival_time
        done_list.append(current)
        if len(done_list) == len(processes):
            return done_list


def RR(processes: list[Process], quantum):
    """
    > The function takes a list of processes and a quantum value, and returns a list of processes in the
    order they were executed

    :param processes: list[Process]
    :type processes: list[Process]
    :param quantum: the time slice for each process
    :return: A list of processes that have been executed in the order they were executed.
    """
    result_list = []
    temp_queue = []
    done_list = []
    current: Process = None
    counter = 0
    works = []
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
            if current not in result_list:
                current.start_time = i
        current.burst -= 1
        counter += 1
        if current.burst == 0:
            works.append(i + 1)
            current.end_time = i + 1
            result_list.append(current)
            current.waiting_time = current.end_time - current.arrival - current.burst
            done_list.append(current)
            counter = 0
            current = None
        else:
            if counter % quantum == 0 and counter != 0:
                works.append(i + 1)
                result_list.append(current)
                temp_queue.append(current)
                current = temp_queue.pop(0)
    return result_list, processes, works


def SRTF(processes: list[Process]):
    """
    It takes a list of processes, sorts them by arrival time, then iterates through the list, keeping
    track of the current process, the previous process, and the processes that have arrived but not yet
    been processed.

    It then finds the process with the shortest burst time, and subtracts one from its burst time. If
    the current process is the same as the previous process, it adds one to the current work time. If
    the current process is different from the previous process, it adds the current work time to the
    list of work times.

    If the current process has a burst time of zero, it removes it from the list of arrived processes
    and adds it to the list of done processes.

    It then increments the arrival time and the current work time.

    If there are no more arrived processes, it sets the end time of the current process to the current
    arrival time, adds the current process to the list of result processes, and

    :param processes: list[Process]
    :type processes: list[Process]
    :return: a tuple of three lists. The first list is a list of processes that have been completed. The
    second list is the original list of processes. The third list is a list of the number of processes
    that were in the ready queue at each time unit.
    """
    processes.sort(key=lambda x: x.arrival)
    works = []
    result_list = []
    arrived = []
    done_list = []
    arrival_time = 0
    prev_current = None
    current = None
    c = 1
    while True:
        arrived.extend([x for x in processes if x.arrival <=
                       arrival_time and x not in done_list and x not in arrived])
        old = current
        current = min(arrived, key=lambda x: x.burst)
        if current != prev_current and prev_current != None:
            prev_current.end_time = arrival_time
            result_list.append(prev_current)
        prev_current = current
        current.burst -= 1
        if old == current:
            works[-1] += 1
        else:
            works.append(c)
        if current.burst == 0:
            arrived.remove(current)
            done_list.append(current)

        arrival_time += 1
        if not arrived:
            current.end_time = arrival_time
            result_list.append(current)
            return result_list, processes, works
        c += 1


def HRRN(processes: list[Process]):
    """
    Calculates the response time for a process, given as (w+b)/b where w is how long the process has waited, and b is the burst time for the process.
    The algorithm then chooses the process with the highest response time, and runs it.
    """
    processes.sort(key=lambda x: x.arrival)
    works = []
    result_list = []
    arrived = []
    done_list = []
    arrival_time = 0
    prev_current = None
    current = None
    c = 1
    while True:
        arrived.extend([x for x in processes if x.arrival <=
                       arrival_time and x not in done_list and x not in arrived])
        old = current
        current = min(arrived, key=lambda x: (x.burst+x.waiting_time)/x.burst)
        if current != prev_current and prev_current != None:
            prev_current.end_time = arrival_time
            result_list.append(prev_current)
        prev_current = current
        current.burst -= 1
        for p in arrived:
            p.waiting_time += 1
        if old == current:
            works[-1] += 1
        else:
            works.append(c)
        if current.burst == 0:
            arrived.remove(current)
            done_list.append(current)

        arrival_time += 1
        if not arrived:
            current.end_time = arrival_time
            result_list.append(current)
            return result_list, processes, works
        c += 1


def NPP(processes: list[Process]):
    arrival_time = 0
    arrived = []
    done_list = []
    works = []
    result_list = []
    current = None
    prev_current = None
    c = 1
    while True:
        arrived.extend([x for x in processes if x.arrival <=
                       arrival_time and x not in done_list and x not in arrived])
        old = current
        current = min(arrived, key=lambda x: x.priority)
        if current != prev_current and prev_current != None:
            prev_current.end_time = arrival_time
            result_list.append(prev_current)
        prev_current = current
        current.burst -= 1
        if old == current:
            works[-1] += 1
        else:
            works.append(c)
        if current.burst == 0:
            arrived.remove(current)
            done_list.append(current)
        arrival_time += 1
        if not arrived:
            current.end_time = arrival_time
            result_list.append(current)
            return result_list, processes, works
        c += 1


def MLM(processes: list[Process]):
    for p in processes:
        p.priority = 1
    arrival_time = 0
    arrived = []
    done_list = []
    works = []
    result_list = []
    current = None
    prev_current = None
    c = 1
    while True:
        arrived.extend([x for x in processes if x.arrival <=
                       arrival_time and x not in done_list and x not in arrived])
        old = current
        current = min(arrived, key=lambda x: x.priority)
        if current != prev_current and prev_current != None:
            prev_current.end_time = arrival_time
            result_list.append(prev_current)
        prev_current = current
        q = min(2 ** (current.priority - 1), current.burst)
        current.burst -= q
        current.priority += 1
        if old == current:
            works[-1] += 1
        else:
            works.append(c)
        if current.burst == 0:
            arrived.remove(current)
            done_list.append(current)
        else:
            arrived.remove(current)
            arrived.append(current)
        arrival_time += q
        if not arrived:
            current.end_time = arrival_time
            result_list.append(current)
            return result_list, processes, works
        c += q


def optimal_end_time(processes: list[Process]):
    for process in processes:
        process.optimal_end_time = process.burst + process.arrival


def pp(processes: list[Process], processes_for_time: list[Process] = None, works=None) -> None:
    if not processes_for_time:
        processes_for_time = processes
    p = [str(x.id).rjust(2) for x in processes]
    if works:
        et = [str(time).rjust(2) for time in works]
    else:
        et = [str(x.end_time).rjust(2) for x in processes]
    avg = sum(x.end_time - x.optimal_end_time for x in processes_for_time) / \
        len(processes_for_time)

    print("Processes (per round)", " | ".join(p))
    print("End times (per round)", " | ".join(et))
    print("average waiting time (per process)", avg)
    # print("Average turnaround time: ", sum(
    # x.turnaround_time for x in processes)/len(processes))


def main():
    string_input = input(
        "Enter processes, format = arrival burst priority, ... ,arrival burst priority: ")
    process_strings = string_input.split(",")
    processes: list[Process] = []
    id = 1
    for process_string in process_strings:
        print(process_string)
        print(process_string.split(" "))
        arrival, burst, priority = process_string.split(" ")
        processes.append(Process(int(arrival), int(burst), id, int(priority)))
        id += 1

    print("FCFS:")
    result = FCFS([copy.copy(x) for x in processes])
    pp(result)
    print("\nSJF:")
    result = SJF([copy.copy(x) for x in processes])
    pp(result)
    print("\nRR:")
    result, result2, works = RR([copy.copy(x) for x in processes], 6)
    pp(result, result2, works)
    print("\nSRTF:")
    result, result2, works = SRTF([copy.copy(x) for x in processes])
    pp(result, result2, works)
    print("\nHRRN:")
    list, list2, works = HRRN([copy.copy(x) for x in processes])
    pp(list, list2, works)
    print("\nNPP:")
    list, list2, works = NPP([copy.copy(x) for x in processes])
    pp(list, list2, works)
    print("\nMLM:")
    list, list2, works = MLM([copy.copy(x) for x in processes])
    pp(list, list2, works)


if __name__ == "__main__":
    main()
