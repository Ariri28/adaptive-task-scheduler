"""
    Manages Task objects and provides scheduling operations.

    The Scheduler demonstrates composition by storing different
    task subclasses and interacting with them through shared behavior.
"""

class Scheduler:

    def __init__(self):
        self.tasks = [] #store all objects managed by scheduler

    def add_task(self, task):  #Add a task object to the scheduler
        self.tasks.append(task) 
        print(f"{task.name} added to scheduler.")


    def display_tasks(self): #Display all tasks currently stored in the scheduler.
        if not self.tasks:
            print("No tasks in the scheduler.")
            return

        print("Tasks in Scheduler:")
        print()

        for task in self.tasks:
            task.display()
            print()


    def remove_task(self, task): #Remove an existing task from the scheduler.
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"{task.name} removed from scheduler.")
        else:
            print("Task not found.")


    def recommend_task(self):   # Recommend the highest-priority unfinished task based on importance.
        best_task = None

        for task in self.tasks:

            if task.completed:
                continue

            if best_task is None:
                best_task = task

            elif task.importance > best_task.importance:
                best_task = task

        return best_task