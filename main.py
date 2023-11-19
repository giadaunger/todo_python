import json

class TodoDatabase:
    def __init__(self) -> None:
        self.todo_list = []
        self.load_todos()

    def load_todos(self):
        with open("todos.json", "r") as f:
            self.todo_list = json.load(f)
            return self.todo_list


class TodoMenu():
    def __init__(self) -> None:
        self.todo_db = TodoDatabase()
        self.start_menu()

    def start_menu(self):
        menu_options = [
            "[1] Show all todos",
            "[2] Add todo",
            "[3] Delete todo / Mark a todo as done",
            "[4] Edit a todo",
            "[q] End the application"
        ]

        while True:
            for menu_option in menu_options:
                print(menu_option)
            
            user_menu_input = input("\nWhat would you like to do? ")

            if user_menu_input == "Q" or user_menu_input == "q":
                pass
            elif user_menu_input == "1":
                pass
            elif user_menu_input == "2":
                pass
            elif user_menu_input == "3":
                pass
            elif user_menu_input == "4":
                pass
            else:
                print("No such option available, please try again!\n")
                input("Press enter to continue")


if __name__ == "__main__":
    menu = TodoMenu()
