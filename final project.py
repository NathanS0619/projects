tasks = [] #create empty list

#menu function
def menu(): #define menu function
    print("Main Menu")
    print("1) Add Task")
    print("2) Delete Task")
    print("3) View Tasks")
    print("4) Exit Program")

#main operation
#choice 1
while True: #create loop while until you exit program
    menu() #call menu
    choice = int(input("Select and option to continue: ")) #create variable for menu selection

    if choice == 1: #user input = 1, add task starts
        print("Add Task")
        task = input("Task to be added: ") #create variable "task" to add to list
        tasks.append(task) #adding task to tasks list
        print("Task added successfully!")
#choice 2
    elif choice == 2: #user input = 2, delete task starts
        print("Delete Task")
        if not tasks: #checking to see if anything is in tasks list
            print("No tasks to delete! Good job!") 
        else: #if there is something in the list, this will run
            try:
                for i, task in enumerate(tasks, start=1): #number the tasks
                    print(f"{i}  {task}") #show the tasks numbered
                delete_index = int(input("Enter the task number you wish to delete: ")) #create variable used to select which task to delete
                if 1 <= delete_index <= len(tasks): #checking to see if the number entered is in the list
                    deleted = tasks.pop(delete_index -1) #actual delete function
                    print(f"Deleted {deleted}") #display message confirming deletion
                else:
                    print("Invalid task number!") #if the number you enter is not there, it will tell you
            except ValueError:
                print("Please enter task number") #if you enter something other than a number, it will tell you
#choice 3
    elif choice == 3: #user selection = 3 start view tasks
            print("View Tasks")
            if not tasks: #checks tasks list to see if there is anything in it
                print("There are no tasks to view! Good job!")
            else: #if there is something in the tasks list this condition starts
                for i, task in enumerate(tasks, start=1): #enumerate the entries in tasks list just like in the delete tasks
                    print(f"{i}  {task}")

#choice 4
    elif choice == 4: #user selection = 4 end the program
            print("Goodbye!")
            break #end loop
