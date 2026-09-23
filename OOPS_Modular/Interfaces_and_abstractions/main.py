from memory_repository import InMemoryTaskRepository
from file_repository import FileTaskRepository
from task_service import TaskService

# --- Using In-Memory Repository ---
print("=== In-Memory Repository ===")
memory_repo = InMemoryTaskRepository()
service1 = TaskService(memory_repo)

service1.create_task("Learn Python")
service1.create_task("Do homework")
service1.show_tasks()

print()

# --- Using File Repository ---
print("=== File Repository ===")
file_repo = FileTaskRepository("tasks.txt")
service2 = TaskService(file_repo)

service2.create_task("Buy groceries")
service2.create_task("Clean room")
service2.show_tasks()

# Notice: TaskService (business logic) is exactly the same in both cases.
# Only the repository (infrastructure) changed. That is the whole point
# of using interfaces / abstraction.
