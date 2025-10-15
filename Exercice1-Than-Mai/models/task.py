""" Import Optional from typing for optional parameter """
from typing import Optional

class Task:
    
    """Represents a task in the ToDoList."""
    """Init a task with its title, optional description, and status (completed or not)."""

    def __init__(self, title: str, description: Optional[str] = None):
        self.title = title
        self.description = description
        self.completed = False

    def task_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔" 
        if self.completed:
            status = "✔"
        else:
            status = "✗"
        return f"[{status}] {self.title} - {self.description if self.description else f'{self.title} - Description none.'}"