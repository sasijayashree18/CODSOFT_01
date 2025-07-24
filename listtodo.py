import os

FILENAME = "todo.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for t in tasks:
            status = "done" if t["done"] else "not"
            f.write(f"{t['task']}|{status}\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i+1}. [{status}] {t['task']}")
        print()

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to mark done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            show_tasks(tasks)
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed['task']}")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Thanks for using To-Do List. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

# Run the program
main()
