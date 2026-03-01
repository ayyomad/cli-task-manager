from manager import TaskManager
from task import Task
def main():
    manager = TaskManager()

    while True:
        print("==== TASK MANAGER ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Complete")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                title = input("Title: ")
                description = input("Description: ")
                priority = input("Priority (low/medium/high): ")
                due_date = input("Due date (optional): ")

                if due_date.strip() == "":
                    due_date = None
                manager.add_task(title, description, priority, due_date)
                print("Task added successfully.")

            case "6":
                print("Exiting...")
                break



if __name__ == "__main__":
    main()