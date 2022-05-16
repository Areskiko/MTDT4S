## What is a process?
A program that is running. It has a PID

Each process has a context which consists of :
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
		3. Other processes
	2. Page daemon

Rest are children of Init.
Every process other than swapper is a child process

Any process that is orphaned (parent is killed, or exits) gets adopted by init

TODO
Zombies

## Unix shells
A shell is a wrapper around the OS core.
Every executed command in a shell is a child process of the shell,
except for internal shell commands (like `cd` and `jobs`)

A child usually blocks the shell from executing more commands

### Standard I/O channels
`stdin` - Standard input channel
`stdout` - Standard output channel
`stderr` - Standard error output channel
...
`files`?

## Process-OS interaction
Code can run in user-mode or kernel-mode, they often change back and forth

Change to kernel mode is usually done via a sys-call

TODO
give examples, [[Fork]], [[Exec]] etc.