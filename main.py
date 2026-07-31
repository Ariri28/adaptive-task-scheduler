from model.task import Task
from model.deadline_task import DeadlineTask
from model.recurring_task import RecurringTask
from model.project_task import ProjectTask
from model.scheduler import Scheduler

"""
Entry point for Adaptive Task Scheduler.

Creates sample tasks, adds them to the Scheduler,
and provides a command-line interface.
"""

def main():

    print("Adaptive Task Scheduler")
    print()

    # Create scheduler
    scheduler = Scheduler()


    # Create Sample Tasks

    task = Task(
        "Programming Language Final Project",
        "2026-07-31 23:59",
        10,
        300
    )


    deadline = DeadlineTask(
        "Submit Assignment",
        "2026-08-01 11:59 PM",
        9,
        120
    )


    recurring = RecurringTask(
        "Exercise",
        "No fixed deadline",
        8,
        30,
        "Daily"
    )


    project = ProjectTask(
        "Adaptive Task Scheduler",
        "2026-07-31",
        10,
        600
    )


    # Add tasks to scheduler

    scheduler.add_task(task)
    scheduler.add_task(deadline)
    scheduler.add_task(recurring)
    scheduler.add_task(project)


    # User Menu

    while True:

        print("\n===== Adaptive Task Scheduler =====")
        print("1. Display Tasks")
        print("2. Recommend Task")
        print("3. Exit")

        choice = input("\nEnter your choice: ")


        if choice == "1":

            scheduler.display_tasks()


        elif choice == "2":

            recommended = scheduler.recommend_task()

            if recommended:
                print("\n=== Recommended Task ===")
                recommended.display()

            else:
                print("\nNo unfinished tasks to recommend.")


        elif choice == "3":

            print("\nGoodbye!")
            break


        else:

            print("\nInvalid choice. Please try again.")



if __name__ == "__main__":
    main()