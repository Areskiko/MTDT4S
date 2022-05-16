## WAIT

The wait(int*) blocks the calling process until one of its child processes terminates. (Immediately if there are no running child processes). Untill the exit status of a terminated process is requested using wait it is categorized as a zombie. A zombies resources can be released, but some information (e.g. status) must be saved.

The return value of wait is the terminated child's PID.

The int * parameter contains the child's 'exit status'.