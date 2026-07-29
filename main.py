from model.task import Task



def main():
    print("Adaptive Task Scheduler")

    task = Task(
        "Programming Language Final Porject", "2026-07-31", 10
    )

    task.display()

    print()

    task.complete_task()

    task.display()


if __name__ == "__main__":
    main()