# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Molly Weaver, 02/14/21,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
taskRow = []    # used for printing
strTask = ""      # Variable to capture a new task
strPriority = ""  # Variable to capture the task's priority
delTask = ""    # Variable to capture a task to delete

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

# creates text file the first time the program is run
objFile = open("ToDoList.txt", "a")
objFile.close()

# open To Do List and read any data into the table
objFile = open("ToDoList.txt", "r")
for row in objFile:
    strData = row.split(",")  # Returns a list from the text file
    dicRow = {strData[0]: strData[1].strip()}  # converts the list to a dictionary
    lstTable += [dicRow]    # adds the dictionary to a table
    dicRow = {}
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Your current task list:")
        for i in range(0, len(lstTable)):
            taskRow = lstTable[i]
            for rowKey, rowValue in taskRow.items():
                print("Task:", rowKey, "|", rowValue, "priority")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Enter the name of the new task: ")
        searchTerm = ""
        # Check to see if task is already in the to do list
        for i in range(0, len(lstTable)):
            searchTerm = strTask
            test = lstTable[i]
            if searchTerm in test:  # If task is in the list go back to menu
                print("That task already exists!")
                searchTerm = "exists"
                break
        if searchTerm == "exists":
            continue
        else:   # If task is not in the to do list, add it
            strPriority = input("Enter the new task's priority (low, medium, or high): ")
            dicRow[strTask] = strPriority
            lstTable += [dicRow]
            print("New task added.")
            dicRow = {}
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        delTask = input("What task would you like to remove?: ")
        searchTerm = ""
        for i in range(0, len(lstTable)):
            searchTerm = delTask
            test = lstTable[i]
            if searchTerm in test:  # If task is in the list delete it
                searchTerm = "exists"
                break
        if searchTerm == "exists":
            del lstTable[i]
            print("Removed", delTask, "from the to do list.")
        else:
            print("That task is not in the list")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for i in range(0, len(lstTable)):
            taskRow = lstTable[i]
            for rowKey, rowValue in taskRow.items():
                objFile.write(rowKey + "," + rowValue + "\n")
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        choice = input("Are you sure you want to exit (Y/N)? ")
        if choice == "N":
            continue
        break  # Exit the program5
