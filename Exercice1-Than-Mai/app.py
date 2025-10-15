""" Flask's modules useful imports"""
from flask import Flask, request, jsonify

""" Controller import from controllers/todo_controller.py """
from controllers.todo_controller import ToDoController

app = Flask(__name__)
controller = ToDoController()

''' CRUD Endpoints for the To-Do List Application '''

@app.route('/tasks', methods=['GET'])
def get_tasks(): # Fetch all tasks
    if not controller.list_tasks():
        return jsonify({"message": "No tasks found in list."})
    tasks = [str(task) for task in controller.list_tasks()]
    return jsonify(tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    title = data.get('title')
    description = data.get('description', None)
    # Check that title is not empty
    if title is None:
        return jsonify({"error": "Title is required."}), 400
    controller.add_task(title, description)
    return jsonify({"message": "Task added!"})

@app.route('/delete-task/<int:idx>', methods=['DELETE'])
def delete_task(idx):
    # Check if index is within range
    if idx < 1 or idx > len(controller.list_tasks()):
        return jsonify({"error": "Task index out of range."}), 400
    # Case where index is not in the list
    if not controller.remove_task(idx - 1):
        return jsonify({"error": "Task index unreachable."}), 400
    return jsonify({"message": "Task deleted!"})

@app.route('/mark-as-completed/<int:idx>', methods=['PUT'])
def mark_as_completed(idx):
    # Check if index is within range
    if idx < 1 or idx > len(controller.list_tasks()):
        return jsonify({"error": "Task index unreachable."}), 400
    # Case where index is not in the list
    if not controller.complete_task(idx - 1):
        return jsonify({"error": "Task index unreachable."}), 400
    return jsonify({"message": "Task marked as completed!"})

""" Ensure that the script does not run when imported elsewhere, but only when executed directly with this file """

if __name__ == "__main__":
    app.run(debug=True)
