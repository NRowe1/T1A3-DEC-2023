### Terminal Application
My application I have created is a task tracker app to help improve productivity, showing tasks completion in order of when they are due.

The features ive included is:
* Task Addition
* Task Listing 
* Task Modification
* Task Completion
* Task Delete
* Search/Filtering


## Menu Page 
The main page is a basic create menu() tag allowing the user to choose what option they want. I added a black font with a white background for the title. I wanted to add a font package but I wasnt able to implement them properly. 
```py
from colored import fg, attr, bg   
# from font_installer import 
from task_functions import add_task, delete_task, view_task, mark_task, search_task, modify_task

import csv 

file_name = "tasks.csv"

try:
    task_file = open(file_name, "r")
    task_file.close()
    print("In try block")
except FileNotFoundError:
    task_file = open(file_name, "w")
    task_file.write("title,completed\n")
    task_file.close()
    print("In except block")

print(f"{fg('black')}{bg('white')}Your task list{attr('reset')}")

def create_menu():
    print("1. Enter 1 to add task to the list")
    print("2. Enter 2 to view your tasks")
    print("3. Enter 3 to modify a task in the list")
    print("4. Enter 4 to mark your task as completed")
    print("5. Enter 5 to delete a task")
    print("6. Enter 6 to search for a task in the list")
    print("7. Enter 7 to exit")

    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "7":
    users_choice = create_menu()
    if users_choice == "1":
        add_task(file_name)
    elif users_choice == "2":
        view_task(file_name)
    elif users_choice == "3":
        modify_task(file_name)
    elif users_choice == "4":
        mark_task(file_name)
    elif users_choice == "5":
        delete_task(file_name)
    elif users_choice == "6":
        search_task(file_name)
    elif users_choice == "7":
        continue
    else:
        print("Invalid Input")
```

## Task Addition 
For the add task users are to enter the task name and the task date
I added a code where the value would have the date be a (int) unfortunatly a string could still be added and I was not able to fix this issue
```py 
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
```

## Task Listing
The List shows the 3 lines of code in the tasks.csv file. First being the list number then the Task name then the date. With those tasks it will say incomplete unless the task is complete which can be changed in the 4th option in the menu.
```py
def view_task(file_name):
    print("View task")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # Check if the row has at least 3 elements
            if len(row) >= 3:
                if row[2] == "True":
                    print(f"Task {row[0]} is complete")
                else:
                    print(f"Task {row[0]} is not complete")
            else:
                print("Invalid row format: ", row)
```

## Task Modification 
This code allows users to change the task name and the task date. A Prompt for both the new Task name and the date. This will modify the task in the tasks.csv file 
```py
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

```

## Task Completion
Going back to the view task command, the task completion will allow for a certain task to be marked as completed. My goal was to have the task say the word "completed" but unfortunatly it says true. Once the task is run in the terminal with the second option being the view command it will say completed or not completed 

```py
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
```

## Task Delete
This command allows for a task to be deleted. Once the promt is shown asking "Enter the task name that you want to remove:" the task will be deleted from the tasks.csv file 
```py
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
```

## Task Search
Finally the search function allows users to search for a specific task in the list.
```py
def search_task(file_name, keyword):
    print(f"Search Task for keyword: {keyword}")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        found_tasks = []
        for row in reader:
            if row and keyword.lower() in [item.lower() for item in row[1:]]:
                found_tasks.append(row)                
        if found_tasks:
            print("Found Tasks:")
            for task in found_tasks:
                print(task)
        else:
            print("No tasks found with the given keyword.")
```


## Packages 
The packages that I have installed is the colored package and the font package

Unfortunatly the font package wasnt able to work 


# Installation
The installation process is very easy all you need to do is open the terminal and type ./run.sh 

This will run and install the packages and then run the Menu once you add a task to the menu it will  update the tasks.csv with a number next to the list. 


### Links

#### youtube
https://youtu.be/XeYnZGMuBUI

#### GIT