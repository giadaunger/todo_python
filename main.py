import database as db
import psycopg2

def list_todos(con):
        todos = db.get_todos(con=con)
        for index, todo in enumerate(todos):
             print(f"[{index}] {todo[1]}")
        input("\nPress enter to go back")


def add_todo(con):
    todo_name = input("Enter a new todo: ")
    categories = db.get_categories(con=con)
    for index, category in enumerate(categories):
        print(f"[{index}] {category[1]}")
    print("[x] Add a new category")

    chosen_category = input("Enter a category: ")

    if chosen_category == "X" or chosen_category == "x":
        pass
    
    try:
        chosen_category = int(chosen_category)
        print(chosen_category)
        correct_choice = categories[chosen_category]
        print(correct_choice[0])
    except (IndexError, ValueError):
            print("\nInvalid input, please enter one of the following choices")

    try:
        db.create_todo(con=con, todo_name=todo_name, category_id=correct_choice[0])
        print(f"{todo_name} was added!")
    except psycopg2.Error:
        input("Something went wrong \nPress enter to continue")


# Main execution logic
def main(con):
    """
    Main menu
    """
    
    menu_text = """
    Welcome!

    [0] List all todos
    [1] Add todo
    [2] Update / Edit todo
    [3] Delete todo
    [q] End program
    """

    menu_choices = {
        "0": list_todos,
        "1": add_todo
    }

    while True:
        print(menu_text)
        choice = input("What would you like to do? ")

        if choice == "q" or choice == "Q":
            return
        
        try:
            menu_choices[choice](con=con)
        except IndexError:
            print("Invalid choice, please enter one of the listed options")


if __name__ == '__main__':
    con = db.connect_db()
    db.create_tables(con=con)
    main(con=con)