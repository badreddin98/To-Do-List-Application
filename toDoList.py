def menu():
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def addTask(tasks):
    title = input("Enter the task title: ")
    tasks.append({"title": title, "status": "Incomplete"})
    print(f'Task "{title}" added successfully!')

def viewTasks(tasks):
    if len(tasks) == 0:
        print("No tasks to show.")
    else:
        index = 0
        while index < len(tasks):
            task = tasks[index]
            print(str(index + 1) + '. ' + task["title"] + ' - ' + task["status"])
            index += 1

def markTaskAsComplete(tasks):
    try:
        taskNumber = int(input("Enter the task number to mark as complete ")) - 1
        if taskNumber >= 0 and taskNumber < len(tasks):
            if tasks[taskNumber]["status"] == "Complete":
                print("Task is already marked as complete.")
            else:
                tasks[taskNumber]["status"] = "Complete"
                print(f'Task "{tasks[taskNumber]["title"]}" marked as complete!')
        else:
            print("Invalid task number, please try again.")
    except ValueError:
        print("Invalid input, please enter a number.")

def deleteTask(tasks):
    try:
        taskNumber = int(input("Enter the task number to delete: ")) - 1
        if taskNumber >= 0 and taskNumber < len(tasks):
            deletedTask = tasks.pop(taskNumber)
            print(f'Task "{deletedTask["title"]}" deleted successfully!')
        else:
            print("Invalid task number, please try again.")
    except ValueError:
        print("Invalid input, please enter a number.")

def main():
    tasks = []

    while True:
        menu()
        try:
            option = input("Select an option 1 - 5: ")
        except ValueError:
            print("Invalid option, please enter a number between 1 and 5.")
            continue

        if option == '1':
            addTask(tasks)
        elif option == '2':
            viewTasks(tasks)
        elif option == '3':
            markTaskAsComplete(tasks)
        elif option == '4':
            deleteTask(tasks)
        elif option == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()