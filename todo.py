

## 1. Project Code (todo.py)


import json
import os

# Task Class
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True


# File Handling
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)


def load_tasks(filename="tasks.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        try:
            return [Task(**data) for data in json.load(f)]
        except json.JSONDecodeError:
            return []


# Display Tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task.completed else "✘ Pending"
        print(f"\n{i}. {task.title} [{task.category}] - {status}")
        print(f"   Description: {task.description}")


# Main CLI
def main():
    tasks = load_tasks()

    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (Work/Personal/Urgent): ")
            tasks.append(Task(title, description, category))
            print("✅ Task added successfully!")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            try:
                task_no = int(input("Enter task number to mark completed: ")) - 1
                if 0 <= task_no < len(tasks):
                    tasks[task_no].mark_completed()
                    print("✅ Task marked as completed!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Enter a valid number.")

        elif choice == "4":
            display_tasks(tasks)
            try:
                task_no = int(input("Enter task number to delete: ")) - 1
                if 0 <= task_no < len(tasks):
                    deleted_task = tasks.pop(task_no)
                    print(f"🗑 Task '{deleted_task.title}' deleted!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Enter a valid number.")

        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Exiting program...")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


