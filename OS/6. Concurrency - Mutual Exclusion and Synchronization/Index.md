##### Henrik er usikker
## Concurrency issues
### Race conditions
A situation that arises from two or more processes/threads trying to update the same shared resource

This may lead to unpredictable results, often depending on which thread does the
updating first

### Critical section
The part of a program that accesses a shared resource,
which may lead to a race condition

## Synchronization
The act of transforming parallel processes to sequential execution

### Locks
A lock is the act of securing a critical section in a manner that ensures that only one thread/process is allowed to access it at the same time.

Examples include binary [[semaphore]]s and [[mutex]]es