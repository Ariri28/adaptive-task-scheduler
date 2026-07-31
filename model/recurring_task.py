from model.task import Task

class RecurringTask(Task):

    def __init__(self, name, deadline, importance, estimated_duration, repeat_frequency ):
        super().__init__(
            name,
            deadline, 
            importance,
            estimated_duration
        )

        self.repeat_frequency = repeat_frequency

    def complete_task(self):
        super().complete_task()
        print(f" {self.name} completed!")