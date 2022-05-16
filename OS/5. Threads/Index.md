## Ok but why threads tho
Another [[OS/4. Processes/Index |process]] would require CPU scheduling,
saving previous context, cop and loading new context

A thread shares code, adata, bss and heap with the main thread,
but *not* the stack, because the thread needs to have independent
flow control, and local variables.

### Advantages of threads
- Less overhead than [[OS/Unix system-calls/Fork]] + [[Exec]]
- Complex operations can be delegated to lightweight helper threads
- Threads kan be used to do longrunning tasks without blocking the main thread of a process

### Dissadvantages of threads
- Errorprone when writing to shared memory TODO shared memory link
	- Critical section
	- Race condition
	- Semaphores
	- Locks

## Fibers
Fibers are user-level threads, which usually ends up as one single thread in kernel space.

### Advantages for fibers
- Extremely fast$^{TM}$ context switch
- No kernel switch

### Disadvantages for fibers
- Blocking of a fiber blocks the entire process
- No speed advantage for multi-processor systems

![[processesvthreadsvfibers.jpg]]

