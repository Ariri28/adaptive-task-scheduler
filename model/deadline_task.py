from model.task import Task

"""
    Represents tasks with a fixed deadline.
    Inherits common task attributes and behavior from Task.
"""

class DeadlineTask(Task):
    def __init__(self, name, deadline, importance, estimated_duration):
        super().__init__(
           name,
           deadline,
           importance,
           estimated_duration 
        )