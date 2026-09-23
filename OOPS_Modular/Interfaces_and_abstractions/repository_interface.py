from abc import ABC, abstractmethod


# This is the interface (abstraction).
# It only tells WHAT a repository should do, not HOW.
# Any class that wants to be a repository must follow this shape.
class TaskRepository(ABC):

    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def get_all_tasks(self):
        pass
