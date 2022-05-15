import math


input_list = []
alloc = int(input("Memory available: "))
number_of_processes = int(input("Enter the number of allocations: "))

for i in range(number_of_processes):
    input_list.append(int(input("Enter memory demand: ")))

