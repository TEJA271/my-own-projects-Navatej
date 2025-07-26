import json
import os

TODO_FILE = "todo_data.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. {status} {task['text']}")

def add_task(tasks):
    task_text = input("Enter a new task: ").strip()
    if task_text:
        tasks.append({"text": task_text, "done": False})
        print("Task added!")

def edit_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Which task number to edit? ")) - 1
        if 0 <= num < len(tasks):
            new_text = input("Enter the new task text: ").strip()
            tasks[num]["text"] = new_text
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Which task number to delete? ")) - 1
        if 0 <= num < len(tasks):
            del tasks[num]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Which task number is done? ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def menu():
    print("""
==== TO-DO LIST MENU ====
1. View tasks
2. Add task
3. Edit task
4. Delete task
5. Mark task as done
6. Save and exit
""")

def main():
    tasks = load_tasks()
    while True:
        menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_done(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

main()
