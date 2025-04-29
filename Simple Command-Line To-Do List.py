# Simple Command-Line To-Do List

todo_list = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("=============================")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list):
            status = "✅" if task['done'] else "❌"
            print(f"{i + 1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title, "done": False})
    print("Task added successfully!")

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]['done'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            deleted = todo_list.pop(index)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! Your tasks will not be saved after exit (unless you use file saving).")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
