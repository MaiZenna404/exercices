""" Importation des modules Flask nécessaires"""
from flask import Flask, request, jsonify
""" Importation du controleur ToDoController """
from controllers.todo_controller import ToDoController

app = Flask(__name__)
controller = ToDoController()

@app.route('/tasks', methods=['GET'])
def get_tasks(): # Récupérer toutes les tasks
    if not controller.list_tasks():
        return jsonify({"message": "Aucune tâche dans la liste."})
    tasks = [str(task) for task in controller.list_tasks()]
    return jsonify(tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    title = data.get('title')
    description = data.get('description', None)
    # Vérifier que title n'est pas vide
    if title is None:
        return jsonify({"error": "Le titre est requis."}), 400
    controller.add_task(title, description)
    return jsonify({"message": "Tâche ajoutée !"})

@app.route('/delete-task/<int:idx>', methods=['DELETE'])
def delete_task(idx):
    # Vérifier que l'index existe bel et bien avant de le supprimer
    if controller.remove_task(idx - 1) is None:
        return jsonify({"error": "Index de tâche invalide."}), 400
    return jsonify({"message": "Tâche supprimée !"})

@app.route('/mark-as-completed/<int:idx>', methods=['PUT'])
def mark_as_completed(idx):
    if controller.complete_task(idx - 1) is None:
        return jsonify({"error": "Index de tâche invalide."}), 400
    return jsonify({"message": "Tâche marquée comme complétée !"})

""" Vérifie si le fichier qui exe le code est bien app.py """
if __name__ == "__main__":
    app.run(debug=True)
