from datetime import datetime

class Task:
    def __init__(self,id,title,description,priority,status="pending",created_at=None,due_date=None):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        if priority.lower() not in ["low","medium","high"]:
            raise ValueError("Invalid priority")
        
        self.id=id
        self.title=title
        self.description=description
        self.priority=priority.lower()
        self.status=status
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.due_date=due_date
    
    def mark_complete(self):
        self.status = "completed"

    def to_dict(self):
         return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "due_date": self.due_date
        }

        

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            status=data["status"],
            created_at=data["created_at"],
            due_date=data.get("due_date")
        )