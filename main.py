from task_functions import add_task, delete_task, mark_task, modify_task, search_task, view_task

file_name = "tasks.csv"

try:
    # open the file in read mode
    task_file = open(file_name, "r")
    task_file.close()
    print("In try block")
    # if it throws error, it means the file doesn't exist
    # if no error, it means the file exist
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create the file
    task_file = open(file_name, "w")
    # We can also insert the first line into the file
    task_file.write("title,completed\n")
    task_file.close()
    print("In except block")


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
    if (users_choice == "1"):
        add_task(file_name)
    elif (users_choice == "2"):
        view_task(file_name)
    elif (users_choice == "3"):
        modify_task(file_name)
    elif (users_choice == "4"):
        mark_task(file_name)
    elif (users_choice == "5"):
        delete_task(file_name)
    elif (users_choice == "6"):
        search_task(file_name)
    elif (users_choice == "7"):
        continue
    else:
        print("Invalid Input")