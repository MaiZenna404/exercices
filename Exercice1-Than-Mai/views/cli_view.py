from controllers.todo_controller import ToDoController

class CLIView:
    """CLI View to interact with the user via command line."""
    def __init__(self):
        self.controller = ToDoController()

    def display_menu(self):
        print("\n--- Bienvenu sur votre gestionnaire de tâches" \
        "\n Que souhaitez-vous faire ? ---")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Afficher les tâches")
        print("4. Marquer une tâche comme terminée")
        print("5. Quitter")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choix : ")
            if choice == "1":
                title = input("Titre : ")
                desc = input("Description (optionnelle) : ")
                self.controller.add_task(title, desc)
                print("Tâche ajoutée !")
            elif choice == "2":
                idx = int(input("Index de la tâche à supprimer : "))
                self.controller.remove_task(idx - 1)
                print("Tâche supprimée !")
            elif choice == "3":
                tasks = self.controller.list_tasks()
                if not tasks:
                    print("Aucune tâche dans la liste.")
                for i, t in enumerate(tasks):
                    print(f"{i + 1}. {t}")
            elif choice == "4":
                idx = int(input("Index de la tâche à compléter : "))
                self.controller.complete_task(idx - 1)
                print("Tâche complétée !")
            elif choice == "5":
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")