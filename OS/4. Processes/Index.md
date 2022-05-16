## What is a process?
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


## Process behaviour and state
### Running
Process is currently being executed on the CPU

A process changing state to running requires a context switch

### Blocked
Process is currently waiting for an I/O operation to complete

### Ready
Process is ready to be run on the CPU

If a process is going from running to ready (without being completed) it is `preempted`

## Unix processess hierarchy
0. Swapper
1. Init
2. Page daemon

Rest are owned by Init 