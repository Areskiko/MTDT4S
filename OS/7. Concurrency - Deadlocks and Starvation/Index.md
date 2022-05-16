## Resources
A resource is administered by the OS, and provided to processes. There are two classes of resources:

### Reusable resources
- Allocated to a process for a certain time
- CPU, main/mass storage, I/O devices...
- Typically synchronized by [[OS/6. Concurrency - Mutual Exclusion and Synchronization/Index | mutual exclusion]]

### Consumable resources
- Generated and destroyed while the system is running.
- Signals, messages, data from input devices...
- Typically synchronized by [[one-sided synchronization]]

## Deadlock
A situation where two or more processes are unable to continue because
both are waiting for a resouce that the other one is holding,
process state is blocked

### Conditions
- Mutual exclusion
	- Only one process may use a resource at a time
- Holding lock for a resouce whilst waiting for another one
- No preemption
	- The OS is unable to forcibly remove a resource from a process

After the conditions are met, circular dependencies can cause a deadlock

### Livelock
Deadlocks when a process uses active waiting.
May lead to extremely poor use of system resources

### Preventative methods
- Invalidate one of the [[#Conditions | deadlock conditions]]
- Prevent circular allocations

### Detection / resolution
- Silently accept deadlocks 'ostrich algorithm'. 
	- Deadlocks are rare, therefore not a big issue
- Search for cycles in waiting graph.
	- May waste system resources

Solutions
- Terminate processes
- Preempt resources
- Virtualization of resources

## Starvation
When a process does not release an allocated resource other waiting processes end up in a locked state, this is called starvation.