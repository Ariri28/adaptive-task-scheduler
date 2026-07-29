class Task: 
    def __init__(self, name, deadline, importance):
        self.name = name
        self.deadline = deadline
        self.importance = importance
        self.completed = False

    def complete_task(self):
        self.completed = True

    def display(self):
        print(f"Task: {self.name}")
        print(f"Deadline: {self.deadline}")
        print(f"Importance: {self.importance}")
        print(f"Completed: {self.completed}")

