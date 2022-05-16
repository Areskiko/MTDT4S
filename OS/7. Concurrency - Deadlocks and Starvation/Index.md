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

### Avoidance
- Invalidate one of the [[OS/7. Concurrency - Deadlocks and Starvation/Index#Conditions]] 
- Prevent circular allocations

## Starvation
When Arran is a dick and doesn't release lock on a resource he is done with