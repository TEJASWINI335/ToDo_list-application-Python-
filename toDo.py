from datetime import datetime

tasks = []

def add_task():
    task = input("Enter the task: ")
    deadline = input("Enter the deadline (DD-MM-YYYY): ")
    
    try:
        deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please enter the date as DD-MM-YYYY.")
        return
    
    tasks.append({"task": task, "deadline": deadline_date, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            completion_status = "Completed" if task['completed'] else "Not Completed"
            print(f"{i}. {task['task']} (Deadline: {task['deadline'].strftime('%d-%m-%Y')}) - {completion_status}")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def show_summary():
    if not tasks:
        print("No tasks available.")
    else:
        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task['completed'])
        print(f"\nSummary: {total_tasks} tasks in total, {completed_tasks} tasks completed, {total_tasks - completed_tasks} tasks pending.\n")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Show Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()






