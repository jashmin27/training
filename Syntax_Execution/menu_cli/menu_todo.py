
tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add task\n2. View tasks\n3. Remove task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
    elif choice == "3":
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
