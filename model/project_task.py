from model.task import Task

class ProjectTask(Task):
    def __init__(self, name, deadline, importance, estimated_duration):
        super().__init__(
            name,
            deadline,
            importance,
            estimated_duration
        )

        self.progress = 0

    def update_progress(self, amount):
        self.progress += amount

        if self.progress > 100:
            self.progress = 100

        if self.progress == 100:
            self.complete_task()

        if self.progress < 0:
            self.progress = 0

        print(f"{self.name} progress: {self.progress}%")
        