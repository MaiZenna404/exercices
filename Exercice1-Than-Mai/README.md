# Exercice1-Nom-Prenom

Small application in Python to manage a ToDo list via command line (CLI) and web API (Flask). Clear architecture (MVC), object-oriented, easy to use and extend.

## Project Structure

```
Exercice1-Nom-Prenom/
├── models/
│   └── task.py           # Task Model
├── controllers/
│   └── todo_controller.py # Workflow logic (add, delete, etc.)
├── views/
│   └── cli_view.py       # CLI Interface
├── app.py                # Flask API entry point
├── main.py               # CLI entry point
└── README.md
```

## Prerequisites

- Python 3.7 or higher
- To install all required libraries at once, use:
  ```bash
  pip install -r allRequirements.txt
  ```
  (Make sure the file `allRequirements.txt` is in the project root and contains all needed packages)

## Utilisation CLI (ligne de commande)

To launch the application in console mode:

```bash
python main.py
```

Follow the on-screen instructions to add, view, delete, or complete tasks.

## API Usage (web mode)

To launch the Flask web server:

````bash
python app.py
```bash
python app.py
````

The API will be accessible at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Main Endpoints

- `GET /tasks` : List all tasks
- `POST /add-task` : Add a task (JSON : `{ "title": "...", "description": "..." }`)
- `DELETE /delete-task/<idx>` : Delete the task at index `<idx>`
- `PUT /mark-as-completed/<idx>` : Mark the task at `<idx>` as completed

## Functionalities

- Add, delete, view, complete tasks
- MVC architecture (separation of model, view, controller)
- REST API with Flask
- Good practices in Python and OOP

## Author

Mai THAN

## GitHub Repo Link

[https://github.com/MaiZenna404/exercices/tree/main/Exercice1-Than-Mai](https://github.com/MaiZenna404/exercices/tree/main/Exercice1-Than-Mai)
