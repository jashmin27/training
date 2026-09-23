# 5.4 Interfaces & Abstraction

## What this task is about
This is a small task to practice ABC (Abstract Base Class) / interfaces
in Python, and to understand how business logic can be kept separate
from infrastructure (like memory storage or file storage).

## Files
- `repository_interface.py` — the interface (abstract class) `TaskRepository`.
  It just defines what methods a repository must have (`add_task`, `get_all_tasks`).
- `memory_repository.py` — first implementation, stores tasks in a Python list.
- `file_repository.py` — second implementation, stores tasks in a text file (`tasks.txt`).
- `task_service.py` — the business logic (`TaskService`). It only uses the
  interface, so it does not care whether tasks are stored in memory or a file.
- `main.py` — runs the demo, using both implementations with the same service.

## How to run
```
python3 main.py
```

## What to notice (Pass condition)
`TaskService` never imports `InMemoryTaskRepository` or `FileTaskRepository`
directly. It only depends on the `TaskRepository` interface. This means we
can swap the storage method (memory, file, or later even a database) without
changing any business logic code. That is what "business logic does not
depend on infrastructure details" means.
