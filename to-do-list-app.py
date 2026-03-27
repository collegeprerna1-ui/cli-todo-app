import json
import os

FILE_NAME = "tasks.json"

# load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    return []
    
# save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks,file,indent=4)

# Add tasks
def add_tasks(tasks):
    task = input("Enter task: ")
    tasks.append({"task":task, "done":False})
    save_tasks(tasks)
    print("Task added!")

# View data
def view_tasks(tasks):
    if not tasks:
        print("No Tasks currently present")
        return
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. [{status}] {t['task']}")

# Mark done 
def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("ENter task nmber to mark done: "))
        tasks[num-1]["done"] = True
        save_tasks(tasks)
        print("Task Completed!")
    except:
        print("Invalid Input")

# Delete Task 
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task Deleted")
    except:
        print("Invalid input")

# Main part 
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO CLI APP ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("choose option: ")

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("GoodBye")
            break
        else:
            print("Invalid Choice")

if __name__ ==  "__main__":
    main()

