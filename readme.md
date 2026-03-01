# CLI Task Manager

First python project
A simple menu based cli task manager

---

# Project Structure

-`main.py` - handles interface
-`manager.py` - handles the managing of the data
-`task.py` - each task is a object

---

## How It Works

- Task data is stored in a single `tasks.json` file.
- On program start:
  - JSON data is loaded.
  - Each dictionary is converted into a `Task` object.
- All operations happen in memory using objects.
- After any change (add, update, delete, mark complete):
  - Task objects are converted back into dictionaries.
  - The JSON file is rewritten.

---

## Run the Project

```bash
python main.py