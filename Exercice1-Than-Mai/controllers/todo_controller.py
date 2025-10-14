from models.task import Task
""" Importation du module List pour typer une liste : List[Type] """
from typing import List

class ToDoController:
    """Contrôleur pour vérifier et gérer la liste de tâches."""
    def __init__(self):
        self.tasks: List[Task] = [] # Liste initialement vide, on ira stocker les tâches ensuite dans une liste.

    def add_task(self, title: str, description: str = None):
        task = Task(title, description)
        self.tasks.append(task)

    """ Si son index est égal à 0 ou moins et est inférieur à la longueur de la liste, on peut supprimer la tâche. """
    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].task_completed() # Marque la tâche sélectionnée 'via son index' comme complétée.
            return list(self.tasks)
        return None