# This is the business logic layer.
# It does NOT know if tasks are stored in memory or in a file.
# It only knows about the TaskRepository interface.
# This is called "dependency boundary" - service is separated from infrastructure.
class TaskService:

    def __init__(self, repository):
        self.repository = repository

    def create_task(self, task_name):
        if task_name == "":
            print("Task name cannot be empty!")
            return
        self.repository.add_task(task_name)
        print(f"Task '{task_name}' added.")

    def show_tasks(self):
        tasks = self.repository.get_all_tasks()
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
