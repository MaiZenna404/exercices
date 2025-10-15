from models.task import Task
""" Import List from typing for Array type hinting """
from typing import List

class ToDoController:
    """Controller to manage the task list."""
    def __init__(self):
        self.tasks: List[Task] = [] # Liste initialement vide, on ira stocker les tâches ensuite dans une liste.

    def add_task(self, title: str, description: str = None):
        task = Task(title, description)
        self.tasks.append(task)

    """ If its index is equal to 0 or more and is less than the length of the list, we can delete the task. """
    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks[index].task_completed() # Mark the selected task 'via its index' as completed.
            return True
        return False