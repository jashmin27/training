# Packages, Imports & Separation of Concerns

## What this task is about
This task takes one messy single-file program (a monolith) and splits it
into separate layers/packages, so each part of the code has one clear job.

## Folder structure
```
before/
  monolithic_app.py      <- old version, everything in one file

after/
  main.py                <- entry point, connects everything
  app/
    config/
      settings.py         <- constants/settings (file name)
    utils/
      helpers.py           <- small helper functions
    repositories/
      expense_repository.py <- reads/writes the data file
    services/
      expense_service.py    <- business rules (e.g. amount > 0), totals
```

## How it was split
- **config** — holds settings like the file name, nothing else.
- **utils** — small reusable helper function (`parse_line`).
- **repositories** — only responsible for saving/loading expenses from the file.
- **services** — business logic (checking valid amount, calculating total).
  It uses the repository but does not know how data is actually stored.
- **main.py** — creates the repository and service, and runs the program.

## How to run
```
cd after
python3 main.py
```

## What to notice (Pass condition)
In the "before" version, everything (settings, file handling, rules,
printing) is in one file, so it's hard to change one part without
affecting the rest. In the "after" version, each layer only depends on
the layer below it (main -> service -> repository -> config/utils),
which makes the project easier to read, test, and maintain.
