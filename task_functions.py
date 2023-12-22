import csv
import os

def add_task(file_name):
    print("Add Task")
    task_name = input("Enter the task name: ")
    task_date = input("Enter the task date: ")

    # Read existing tasks to determine the next task number
    task_number = 1
    existing_tasks = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # Check if the row is not empty and the value in row[0] is convertible to int
            if row and row[0].isdigit():
                task_number = max(task_number, int(row[0]) + 1)

    # Append the new task to the list with the next task number
    new_task = [str(task_number), task_name, task_date]

    # Write the updated task list to the CSV file
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_task)
        print("Mark Task")

def delete_task(file_name):
    print("Delete Task")
    task_name = input("Enter the task name that you want to remove: ")
    
    # Copy all the contents of the CSV into a new list
    # While doing this, we constantly check for the condition
    # When we encounter the todo to be removed, we don't copy that one
    # The final new todo will be written in the CSV file
    task_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # Check if the row is not empty and task_name is not equal to row[1]
            if row and task_name != row[1]:  # Assuming task_name is in the second column (index 1)
                task_lists.append(row)

    # Write the updated task list to the CSV file
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(task_lists)

def view_task(file_name):
    print("View todo")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # row = ["Todo 1", "False"]
            if (row[1] == "True"):
                print(f"Todo {row[0]} is complete")
            else:
                print(f"Todo {row[0]} is not complete")

                
def modify_task(file_name):
    print("Modify Task")
    task_name = input("Enter the task name that you want to modify: ")

    tasks = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 3 and task_name == row[1]:
                new_task_name = input("Enter the new task name: ")
                new_task_date = input("Enter the new task date: ")
                row[1] = new_task_name
                row[2] = new_task_date
            tasks.append(row)

    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

def mark_task(file_name):
    print("Mark task")
    task_name = input("Enter the task name that you want to mark as complete: ")
    tasks = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 3 and task_name == row[1]:
                row[2] = "completed"  # Set to the desired word
            tasks.append(row)
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

# def search_task(file_name, keyword):
#     print(f"Search Task for keyword: {keyword}")
#     with open(file_name, "r") as f:
#         reader = csv.reader(f)
#         found_tasks = []
#         for row in reader:
#             if row and keyword.lower() in [item.lower() for item in row[1:]]:
#                 found_tasks.append(row)                
#         if found_tasks:
#             print("Found Tasks:")
#             for task in found_tasks:
#                 print(task)
#         else:
#             print("No tasks found with the given keyword.")