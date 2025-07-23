import pandas, csv


def read_tasks_from_csv_file():
    data = pandas.read_csv("To-Do List.csv")
    tasks = data["Tasks"].to_list()
    return tasks


def update_csv_file(new_tasks):
    tasks_dict = {
        "Tasks": new_tasks
    }
    data = pandas.DataFrame(tasks_dict)
    data.to_csv("To-Do List.csv")


def add_task():
    new_task = input("Enter task you want to add : ").title()
    tasks = read_tasks_from_csv_file()
    tasks.append(new_task)
    update_csv_file(tasks)
    print(f"Task '{new_task}' has been successfully added.")
    return 0


def update_task():
    updated_task = input("Enter the task name you want to update : ").title()
    tasks = read_tasks_from_csv_file()
    if updated_task in tasks:
        new_task = input("Enter new task = ")
        ind = tasks.index(updated_task)
        tasks[ind] = new_task
        update_csv_file(tasks)
        print(f"Updated task '{updated_task}' to '{new_task}'.")
    else:
        print("Task not found.")
    return 0


def delete_task():
    deleted_task = input("Which task you want to delete : ").title()
    tasks = read_tasks_from_csv_file()
    print(tasks)
    if deleted_task in tasks:
        ind = tasks.index(deleted_task)
        del tasks[ind]
        update_csv_file(tasks)
        print(f"Task '{deleted_task}' has been deleted.")
    else:
        print("Task not found.")
    return 0


def view_tasks():
    tasks = read_tasks_from_csv_file()
    cnt = 0
    for task in tasks:
        cnt += 1
        print(f"{cnt}- {task}")
    print('\n')
    return 0


def exit_the_program():
    print("Closing the program....")
    return 1


with open("To-Do List.csv", mode="w") as data_file:
    pass

new_tasks = []
tasks_number = int(input("Enter the number of tasks : "))
for i in range(tasks_number):
    task_name = input(f"Enter task {i + 1} : ").title()
    new_tasks.append(task_name)

update_csv_file(new_tasks)

print(f"Today's tasks are : ")
view_tasks()

operations = {
    "1": ('Add', add_task),
    "2": ('Update', update_task),
    "3": ('Delete', delete_task),
    "4": ('View', view_tasks),
    "5": ('Exit', exit_the_program)
}

while True:

    print("The operations :")

    for key in operations:
        print(f"{key}- {operations[key][0]}")

    operation = input("Enter the number of the operation you want to perform : ")
    try:
        operation_function = operations[operation][1]
        if operation_function():
            break
    except:
        print("Invalid Input. Please enter a valid number.")
