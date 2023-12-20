import csv
import os 

# def add_task(file_name):
#     print("Add task")
#     # Ask the title of the todo
#     task_name = input("Enter a todo: ")
#     task_date = input("Enter the date: ")
#     # Open file - list.csv
#     with open(file_name, "a") as f:
#         writer = csv.writer(f)
#         # Insert values - title = user entered
#                       # - completed = False
#         writer.writerow([task_name, task_date])

def view_task(file_name):
        print("View Task")
def modify_task(file_name):
        print("Modify Task")
def mark_task(file_name):
        print("Mark Task")

def delete_task(file_name):
    print("Delete Task")
    task_name = input("Enter the todo name that you want to remove: ")
    
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

def add_task(file_name):
    print("Add Task")
    task_name = input("Enter the todo name: ")
    task_date = input("Enter the todo date: ")

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

# Example usage
delete_task("tasks.csv")
add_task("tasks.csv")



def search_task(file_name):
        print("Search for a task")


# def mark_todo(file_name):
#     print("Mark todo")
#     task_name = input("Enter the todo name that you want to mark as complete: ")
#     task_lists = []
#     with open(file_name, "r") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if (task_name != row[0]):
#                 task_lists.append(row)
#             else:
#                 task_lists.append([row[0], "True"])
#     with open(file_name, "w") as f:
#         writer = csv.writer(f)
#         writer.writerows(task_lists)

# def view_todo(file_name):
#     print("View todo")
#     with open(file_name, "r") as f:
#         reader = csv.reader(f)
#         reader.__next__()
#         for row in reader:
#             # row = ["Todo 1", "False"]
#             if (row[1] == "True"):
#                 print(f"Todo {row[0]} is complete")
#             else:
#                 print(f"Todo {row[0]} is not complete")