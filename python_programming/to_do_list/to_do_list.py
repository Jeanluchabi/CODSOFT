import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_id = len(tasks) + 1
    description = input("Enter task description: ")
    priority = input("Enter task priority (low, medium, high): ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    status = False
    tasks.append({
        'id': task_id,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'status': status
    })
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Completed" if task['status'] else "Pending"
        print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = input("Enter new task description: ")
            task['priority'] = input("Enter new task priority (low, medium, high): ")
            task['due_date'] = input("Enter new task due date (YYYY-MM-DD): ")
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return
    print("Task not found.")

def mark_task_completed(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = True
            save_tasks(tasks)
            print("Task marked as completed!")
            return
    print("Task not found.")

def main():
    print("Starting To-Do List application...")
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
