### Which abstractions does a modern OS provide?
- Multiprogramming
	- Only one instruction pointer
	- Context switching
- Concurrent Processes
	- Independent sequential control flows
- CPU Multiplexing
	- Only one process active at any time (single processer system)

### What is a process?
A program that is running.

This requires process context which consists of :
- Memory
	- Code
	- Data
	- General Purpose Registers
		- Instruction Pointer
		- Stack Pointer
	- Stack
- Process State
- User Id
- Access Permissions
- Resources
	- Files
	- I/O Devices
	- etc.

Memory og resources ligger i en process control block (PCB)
### Process behaviour and state
#### Running
Process is currently being executed on the CPU

	A process changing state to running requires a context switch

#### Blocked
Process is currently waiting for an I/O operation to complete

#### Ready
Process is ready to be run on the CPU