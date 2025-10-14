""" Importation du modèle qui permet à un attribut d'être optionnel """
from typing import Optional

class Task:
    """Représente une tâche de la ToDoList."""
    """Init une tâche avec son title, description [optionnelle] et son statut (complétée ou non)."""
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
        return f"[{status}] {self.title} - {self.description if self.description else f'{self.title} n\'a pas encore été complétée.'}"