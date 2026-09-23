from repository_interface import TaskRepository


# Implementation 2: keeps tasks in a text file.
# Data stays saved even after the program stops.
class FileTaskRepository(TaskRepository):

    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        # make sure the file exists
        open(self.filename, "a").close()

    def add_task(self, task):
        with open(self.filename, "a") as f:
            f.write(task + "\n")

    def get_all_tasks(self):
        with open(self.filename, "r") as f:
            lines = f.readlines()
        # remove the newline character from each line
        return [line.strip() for line in lines]
