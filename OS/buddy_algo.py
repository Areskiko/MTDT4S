import math


alloc = int(input("Memory available: "))
size_of_block = int(input("Size of block: "))
input_list = list(map(int, input("Enter demands (space seperated): ").split()))

memory_list = [0] * (alloc // size_of_block)


def check_can_set(number_of_blocks, memory_list, i):
    for j in range(i, i+number_of_blocks):
        if memory_list[j] != 0:
            return False
    return True


for i in range(len(input_list)):
    a = input_list[i]
    exponent = math.ceil(math.log2(input_list[i]))
    size_of_process = 2 ** exponent
    number_of_claimed_blocks = math.ceil(size_of_process / size_of_block)
    flag = -1
    for j in range(len(memory_list)):
        if memory_list[j] == 0 and check_can_set(number_of_claimed_blocks, memory_list, j) and j*size_of_block % size_of_process == 0:
            flag = j
            for k in range(j, j+number_of_claimed_blocks):
                memory_list[k] = 1
            break
    if flag == -1:
        print("Not enough memory for process", a)
    else:
        print("Process", a, "is allocated at", flag*size_of_block, "with size", size_of_process)



print("\nMemory List: ", memory_list)
