class Scheduler:

    def __init__(self):
        self.tasks = [] #store all objects managed by scheduler

    #Add task

    def add_task(self, task):
        self.tasks.append(task) 
        print(f"{task.name} added to scheduler.")

    #Task display

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the scheduler.")
            return

        print("Tasks in Scheduler:")
        print()

        for task in self.tasks:
            task.display()
            print()

    #Removal of existing tasks in scheduler

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"{task.name} removed from scheduler.")
        else:
            print("Task not found.")

    #High-priority task tracking

    # Recommend the highest-priority unfinished task based on importance.
    def recommend_task(self):
        best_task = None

        for task in self.tasks:

            if task.completed:
                continue

            if best_task is None:
                best_task = task

            elif task.importance > best_task.importance:
                best_task = task

        return best_task