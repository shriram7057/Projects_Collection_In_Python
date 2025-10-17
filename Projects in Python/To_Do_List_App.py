# todo_list.py
tasks = []

def show_tasks():
    print("\n📋 To-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

while True:
    print("\n1. Add Task  2. View Tasks  3. Exit")
    ch = input("Choose: ")
    if ch == "1":
        tasks.append(input("Enter task: "))
    elif ch == "2":
        show_tasks()
    else:
        break
