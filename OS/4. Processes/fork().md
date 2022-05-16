# fork()

From the point of view of the application, calling fork looks like a regular function call

`pid = fork()`

#### fork creates a new child process

- Duplicates the calling process (the standard way to create new processes in Unix!)

-  The child process inherits… 
	- Address space (code, data, bss, stack segments)
	- User and group ID
	- Standard I/O channels
	- Process group, signal table
	- Open files, current working directory

- Not copied are the following:
	- Process ID (PID), parent process ID (PPID)
	- Pending signals, accounting data, ...

#### One process calls fork, but two processes return
- We can use this to differentiate between the child and parent process
- Parent process: `pid = (childs new pid)`
- Child process: `pid= 0`
(*NB!* these pids are not the actual process-IDs of the parent and child, but rather the variables that are in the code)



## Fast process creation
- Copying the address space takes a lot of time
	- Especially if the program immediately calls [[Exec |exec..()]] afterwards
	  ➛ complete waste of time!
- Historic solution: vfork
	- The parent process is suspended until the child process calls exec..() or terminates using \_exit()
- The child simply uses code and data of its parent (without copying!)
	- The child process must not change any data
	- sometimes not so simple: e.g., don’t call exit(), but \_exit()!
- Modern solution: copy on write

### Copy on write
- Parent and child process share the same code and data segments using the memory management unit (MMU)
- Copy on write needs some hardware support

- A segment is copied only if the child process changes any data
	- If a child only reads data nothing really happens
	- Only when a child writes we need to copy the data, but not everything only the affected page

- You dont use any copy on write functionality when exec..() is called directly after fork()

- fork() using copy on write is almost as fast as vfork()

