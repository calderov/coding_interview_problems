# Implement a tasks scheduling system with the following methods:

# add_task(task_id: str, priority: int)
#   Adds a task with a given task_id and integer priority.
#   Higher priority means the task should be run sooner.
#   If two tasks have the same priority, the one added earlier should run first.

# get_next_task() -> str
#   Returns the task_id of the task that should run next, removing it from the scheduler.

# cancel_task(task_id: str) -> bool
#   Removes the task with the given task_id from the scheduler if it exists.
#   Returns True if the task was removed, False otherwise.

from heapq import *

class TasksScheduler:
    def __init__(self):
        self.tasks = []
        self.t = 0

    def add_task(self, task_id, priority):
        heappush(self.tasks, (-priority, self.t, task_id))
        self.t += 1

    def get_next_task(self):
        if not self.tasks:
            return None
        
        # Find tasks with the highest priority
        priority = self.tasks[0][0]
        buffer = []

        while self.tasks and self.tasks[0][0] == priority:
            _, t, task_id = heappop(self.tasks)
            heappush(buffer, (t, task_id))

        # Get task_id of task with the lowest t
        _, next_task_id = heappop(buffer)

        # Move remaining tasks in buffer back to tasks heap
        while buffer:
            t, task_id = heappop(buffer)
            heappush(self.tasks, (priority, t, task_id))

        return next_task_id

    def cancel_task(self, task_id):
        task_id_index = -1
        
        for i in range(len(self.tasks)):
            _, _, current_task_id = self.tasks[i]
            if task_id == current_task_id:
                task_id_index = i
                break
        
        if task_id_index == -1:
            return False
        
        del self.tasks[task_id_index]
        heapify(self.tasks)

        return True

if __name__ == "__main__":
    scheduler = TasksScheduler()

    print('Result:')
    scheduler.add_task('Task 1', 1)
    scheduler.add_task('Task 2', 1)
    scheduler.add_task('Task 3', 1)
    scheduler.add_task('Task 4', 0)
    scheduler.add_task('Task 5', 2)
    scheduler.add_task('Task 6', 0)
    scheduler.add_task('Task 7', 0)

    print(scheduler.get_next_task())
    print(scheduler.get_next_task())
    print(scheduler.get_next_task())
    
    print(scheduler.cancel_task('Task 6'))
    print(scheduler.cancel_task('Task 7'))

    print(scheduler.cancel_task('Task 8'))

    print('\nExpected:')
    print('Task 5')
    print('Task 1')
    print('Task 2')
    print('True')
    print('True')
    print('False')
