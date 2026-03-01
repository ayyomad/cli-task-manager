import os
import json
from task import Task
class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = []
        self.next_id = 1
        self.load_from_file()

    def load_from_file(self):
        self.tasks = []

        if not os.path.exists(self.file_path):
            with open(self.file_path,"w") as f:
                json.dump([], f)
        
        try :
            with open(self.file_path,"r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data=[]
        
        for item in data:
            task=Task.from_dict(item)
            self.tasks.append(task)
        if not self.tasks:
            self.next_id=1
        else:
            self.next_id=max(task.id for task in self.tasks) + 1

    def add_task(self, title, description, priority, due_date=None):
        task = Task(self.next_id, title, description, priority, due_date=due_date)
        self.tasks.append(task)
        self.next_id += 1
        self.save_to_file()

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_to_file()
            return True
        return False
    
    def mark_complete(self, task_id):
        task=self.get_task_by_id(task_id)
        if task:
            task.mark_complete()
            self.save_to_file()
            return True
        return False
            

    def update_task(self, task_id, title=None, description=None, priority=None, due_date=None):
        task=self.get_task_by_id(task_id)
        if task:
            if title is not None and title.strip():
                task.title = title.strip()

            if description is not None:
                task.description = description

            if priority is not None:
                normalized = priority.strip().lower()
                if normalized in ["low", "medium", "high"]:
                    task.priority = normalized
                    
            if due_date is not None:
                task.due_date = due_date
            self.save_to_file()
            return True
        return False

   

    def save_to_file(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.file_path,"w") as f:
            json.dump(data, f, indent=4)
