## WAIT

The wait(int*) blocks the calling process until one of its child processes terminates. (Immediately if there are no running child processes)

The return value of wait is the terminated child's PID.

The int * parameter contains the child's 'exit status'.