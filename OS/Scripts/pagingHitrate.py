requests = [1, 3, 5, 4, 2, 4, 3, 2, 1, 0, 5,
            3, 5, 0, 4, 3, 5, 4, 3, 2, 1, 3, 4, 5]


def fifo(available_pages: int):
    """
    FIFO page replacement algorithm
    :param available_pages:
    :return:
    """
    page_table = []
    num_page_faults = 0
    for request in requests:
        if request in page_table:
            print(page_table)
            continue
        num_page_faults += 1
        if len(page_table) == available_pages:
            page_table.pop(0)
        page_table.append(request)
        print(page_table)

    print(f"Number of page faults: {num_page_faults}")
    
    hit_rate = (len(requests) - num_page_faults) / len(requests)
    print(f"Hit rate: {hit_rate}")
    
def lru(available_pages: int):
    """
    LRU page replacement algorithm
    :param available_pages:
    :return:
    """
    page_table = []
    num_page_faults = 0
    for request in requests:
        if request in page_table:
            page_table.remove(request)
            page_table.append(request)
            print(page_table)
            continue
        num_page_faults += 1
        if len(page_table) == available_pages:
            page_table.pop(0)
        page_table.append(request)
        print(page_table)
    
    print(f"Number of page faults: {num_page_faults}")
    
    hit_rate = (len(requests) - num_page_faults) / len(requests)
    print(f"Hit rate: {hit_rate}")

def optimal(available_pages: int):
    """
    Optimal page replacement algorithm
    :param available_pages:
    :return:
    """
    page_table = []
    num_page_faults = 0
    for idx, request in enumerate(requests):
        if request in page_table:
            print(page_table)
            continue
        num_page_faults += 1
        if len(page_table) == available_pages:
            # ser frem i tid og fjerner den pagen 
            # som skal brukes lengst frem i tid. 
            request_set = set(page_table)  
            for i in range(idx, len(requests)):
                if requests[i] in request_set:
                    request_set.remove(requests[i])
                if len(request_set) == 1:
                    break       
            page_table.remove(request_set.pop())
        page_table.append(request)
        print(page_table)

    print(f"Number of page faults: {num_page_faults}")
    print(f"Hit rate: {(len(requests) - num_page_faults) / len(requests)}")

lru(5)
optimal(5)
fifo(5)