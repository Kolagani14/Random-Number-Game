tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                print(f"Deleted task: {removed}")
            except:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting... Bye 👋")
        break

    else:
        print("Invalid choice. Try again.")


items=[]
while True:
    print("Food menu")
    print("1.Add items")
    print("2.read items")
    print("3.delete items")
    print("4.Exit the table")
    
    options=input("Enter yours options:")
    if options=="1":
        item=input("enter the item: ")
        items.append(item)
        print("item add succefully")
    
    elif options=="2":
        if item not in items:
            print("items are not availble")
        for i,item in enumerate(items,start=1):
            print(i,".",item)
    elif options=="3":
        if not  items:
            print("no items are not to delete")
        else:
            for i,item in enumerate(items,start=1):
                print(i,".",item)
            if items:
                n=int(input("enter the item number"))
                rem=items.pop(n-1)
                print("item was deleted:",rem)
            else:
                print("not valid")
    elif options == "4":
        print("bill please")
        print("we are off to the table")
    else:
        print("invalid choice")
                
        
 