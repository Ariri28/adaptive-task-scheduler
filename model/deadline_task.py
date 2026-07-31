from model.task import Task

class DeadlineTask(Task):
    def __init__(self, name, deadline, importance, estimated_duration):
        super().__init__(
           name,
           deadline,
           importance,
           estimated_duration 
        )