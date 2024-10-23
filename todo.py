import os
import json

# File to store tasks
FILE_NAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{idx}. {task['task']} - {status}")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark complete: "))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

menu()
