from repository_interface import TaskRepository


# Implementation 1: keeps tasks in a normal Python list.
# Data is lost when the program stops.
class InMemoryTaskRepository(TaskRepository):

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks
