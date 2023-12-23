import keyword
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
        search_task(file_name, keyword)
    elif users_choice == "7":
        continue
    else:
        print("Invalid Input")