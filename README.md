## ABOUT

This was a project for my CSC 400 (Operating Systems) class. The idea of the project was to implement a scheduler that randomly selected tasks to complete based on their priority (0-15). It would also generate a random I/O probability between 0 and 1 to decide if the chosen process will be blocked after running or not. The program will run for 10,000 time units before stopping and printing the number of times a task ran at each priority level.

## FULL TASK

#### Implement a scheduler (in either Java or Python) with the following rules:
1. Initialize the system with 40 processes, each with a random priority between 4 and 10.  Also assign each process a random I/O probability ranging from 0 to .99999….
2. The scheduler is priority-based, with priorities ranging from 0 (lowest) to 15 (highest).  The highest priority process that is ready to run will be scheduled next.  If there are multiple processes at the same priority, they will be scheduled in a round-robin fashion.
3. If there are no processes that are ready to run, then the CPU will remain idle.
4. When a process is scheduled:
   - Randomly choose a value between 0 and 1, and if this value is less than the I/O probability for this process, the process will block after this time unit is over.  When this occurs, randomly choose a value between 5 and 20 to determine the number of time slots that this process will be blocked.  After it is ready to run again, the priority should be raised by 1 (unless it is already 15).
   - The remaining time the process uses the entire time slot without blocking.  In this case, the priority of the process should be decreased by 1 (unless it is already 0)
5. After 10,000 time units, the system should stop and output for each priority level, the number of times that a process with that priority was scheduled.


## INSTRUCTIONS

1. Download and run the CSC400Project.py file
2. The program will output the number of times each process was scheduled.
3. Run the file as many times as wanted to get new results
