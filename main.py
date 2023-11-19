class TodoDatabase:
    def __init__(self) -> None:
        self.todo_list = []


class TodoMenu():
    def __init__(self) -> None:
        todo_db = TodoDatabase()
        self.start_menu()

    def start_menu(self):
        menu_options = [
            "[1] Show todos",
            "[2] Add todo",
            "[3] Delete todo / Mark a todo as done",
            "[4] Edit a todo"
        ]

        while True:
            for menu_option in menu_options:
                print(menu_option)
            
            user_menu_input = input("\nWhat would you like to do? ")


if __name__ == "__main__":
    menu = TodoMenu()
