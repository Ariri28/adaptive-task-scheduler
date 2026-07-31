"""
Base task class representing common task attributes and behavior.
"""

class Task: 
    def __init__(self, name, deadline, importance, estimated_duration):
        self.name = name
        self.deadline = deadline
        self.importance = importance
        self.estimated_duration = estimated_duration
        self.completed = False

    def complete_task(self):
        self.completed = True

    def display(self):
        print(f"Task: {self.name}")
        print(f"Deadline: {self.deadline}")
        print(f"Importance: {self.importance}")
        print(f"Estimated Duration: {self.estimated_duration} minutes")
        print(f"Completed: {self.completed}")

