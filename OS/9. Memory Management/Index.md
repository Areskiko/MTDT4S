## Title (din sopp)
Multiple processses need main memory that can be located in different parts of the memory,
therefore the OS needs to know about the following:

- Free memory space
- Allocated memory space
- Fragmentation size
- What type of memory should each process be in
	- Cache
	- Ram
	- Drive

## Memory allocation techinques
### Bitlist
#### Strategy
List 'em bits
Array containing wether a part of the memory is free or allocated

#### Problems
- The bitlist itself requires a lot of memory
- Linear search is slow

#### Used by
Secondary storage

### Linkedlist 1
#### Strategy
It has a pointer to each start and length of both allocated and free memory

#### Problems
Memory for list has to be allocated dynamically

#### Used by
Management of heap memory (malloc and libc functions)

### Linkedlist 2
#### Strategy
It has a pointer to the start and length of every free memory segment

#### Problems
Memory for list has to be allocated dynamically

#### Used by
Management of heap memory (malloc and libc functions)

## Memory placement strategies
### First fit
#### Strategy
Use the first fitting gap

#### Problem
Creates  a large number of small gaps at the beginning of memory

### Rotating fit / Next fit
#### Strategy
Like [[OS/9. Memory Management/Index#First fit]] but starting from the most recently
allocated gap

#### Problem
None

### Best fit
#### Strategy
Find the smalles fitting gap

#### Problem
Possible fragmentation

### Worst fit
#### Strategy
Find the largest fitting gap

#### Problem
None

### Buddy method
#### Strategy
Split memory dynamically into areas of powers of two

#### Problem
None

#### Used by
System memory, allocation of memory to User and System processes

## Fragmentation
### External
Allocation creates fragmentation outside the allocated area, which cannot be used

Occurs with [[OS/9. Memory Management/Index#First fit]] and [[OS/9. Memory Management/Index#Best fit]]
### Internal
Unused memory inside allocated area

Occurs with [[OS/9. Memory Management/Index#Buddy method]]
due to rounding up to nearest power of two

## Swapping
Segments of aprocess are released from memory and swapped out to background memory.
Usually happens if I/O operations hinder a process from running

Segments are swapped back into memory when waiting times end

### Bottleneck
The read/write rates of swap medium (swap file, partition, etc.)