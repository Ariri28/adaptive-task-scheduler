from model.task import Task
from model.deadline_task import DeadlineTask
from model.recurring_task import RecurringTask
from model.project_task import ProjectTask
from model.scheduler import Scheduler

def main():
    print("Adaptive Task Scheduler")
    print()

    #create scheduler
    scheduler = Scheduler()

    #create Tasks

    #Base Task

    task = Task(
        "Programming Language Final Project", "2026-07-31 23:59", 10, 300
    )

    
    #Deadline Task
    deadline = DeadlineTask(
        "Submit Assignment", "2026-08-01 11:59 PM", 9, 120
        )
    
   

    print()

    #Recurring Task

    recurring = RecurringTask(
        "Exercise", "No fixed deadline", 8, 30, "Daily"
    )

 


    print()
   

    #Project Task

    project = ProjectTask(
        "Adaptive Task Scheduler", "2026-07-31", 10, 600
    )

    print("=== Project Task ===")

    #project progress
    project.update_progress(25)
    project.update_progress(30)
    project.update_progress(45)

    print()
    
    # Add tasks to the scheduler
    scheduler.add_task(task)
    scheduler.add_task(deadline)
    scheduler.add_task(recurring)
    scheduler.add_task(project)

    print()

    # Display all tasks
    scheduler.display_tasks()

    print("Removing Exercise...\n")

    # Remove one task
    scheduler.remove_task(recurring)

    print()

    # Display remaining tasks
    scheduler.display_tasks()

    recommended = scheduler.recommend_task()

    if recommended:
        print("\nRecommended Task:")
        recommended.display()
    else:
        print("\nNo unfinished tasks to recommend.")


if __name__ == "__main__":
    main()
    