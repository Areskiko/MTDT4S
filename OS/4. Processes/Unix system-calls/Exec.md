## EXEC

Exec() is a family of functions which replaces the currently executable file with a new executable file. The entire content of the process is replaces with a new program.

- [PID] of the process is not changed but the data, code, stack, heap, etc. of the process are changed and are replaced with those of newly loaded process. 
- The new process is executed from the entry point.
- The new process is loaded into the same process space
- The currently running process is ended

#### The standard names for the exec() functions:
1.  execl
2.  execle
3.  execlp
4.  execv
5.  execve
6.  execvp

#### Exec() followed by these letters:
**e**: It is an array of pointers that points to environment variables and is  passed explicitly to the newly loaded process.

**l**: l is for the command line arguments passed a list to the function

**P**: p is the path environment variable which helps to find the file passed as an argument to be loaded into process.

**v**: v is for the command line arguments. These are passed as an array of pointers to the function.