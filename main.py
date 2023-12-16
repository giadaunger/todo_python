import database as db
import psycopg2

def list_todos(con):
        todos = db.get_todos(con=con)
        for index, todo in enumerate(todos):
             print(f"[{index}] {todo[1]}")
        input("\nPress enter to go back")


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
        "0": list_todos
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