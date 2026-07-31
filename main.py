from model.task import Task
from model.deadline_task import DeadlineTask
from model.recurring_task import RecurringTask
from model.project_task import ProjectTask

def main():
    print("Adaptive Task Scheduler")
    print()

    #Base Task

    task = Task(
        "Programming Language Final Project", "2026-07-31 23:59", 10, 300
    )

    print("== Base Task ==")

    task.display()

    task.complete_task()

    task.display()

    print()

    #Deadline Task
    deadline = DeadlineTask(
        "Submit Assignment", "2026-08-01 11:59 PM", 9, 120
        )
    
    print("=== Deadline Task ===")
    deadline.display()

    print()

    #Recurring Task

    recurring = RecurringTask(
        "Exercise", "No fixed deadline", 8, 30, "Daily"
    )

    print("=== Recurring Task ===")
    recurring.display()
    recurring.complete_task()

    print()
   

    #Project Task

    project = ProjectTask(
        "Adaptive Task Scheduler", "2026-07-31", 10, 600
    )

    print("=== Project Task ===")
    project.display()

    project.update_progress(25)
    project.update_progress(30)
    project.update_progress(45)

    

if __name__ == "__main__":
    main()