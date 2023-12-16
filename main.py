import database as db
import psycopg2

def list_todos(con):
        todos = db.get_todos(con=con)
        for index, todo in enumerate(todos):
            print(f"[{index}] {todo[1]} - {todo[4]}")
        input("\nPress enter to go back")


def add_todo(con):
    while True:
        todo_name = input("Enter a new todo: ").capitalize()
        if len(todo_name) < 2:
            print("Todo name too short, try again! ")
            continue
        elif len(todo_name) > 100:
            print("Todod name too long, try again! ")
            continue
        break

    while True:
        categories = db.get_categories(con=con)
        for index, category in enumerate(categories):
            print(f"[{index}] {category[1]}")
        print("[x] Add a new category")

        chosen_category = input("Enter a category: ")

        if chosen_category == "X" or chosen_category == "x":
            while True:
                new_category_name = input("Enter a new category: ").capitalize()
                if len(new_category_name) < 2:
                    print("Category name too short, try again! ")
                    continue
                elif len(new_category_name) > 100:
                    print("Category name too long, try again! ")
                    continue

                category_exists = False
                for category in categories:
                    if new_category_name == category[1]:
                        print("\nCategory already exists, try again!")
                        category_exists = True
                        break  

                if category_exists:
                    continue  
                else:
                    db.create_category(con=con, category_name=new_category_name)
                    print(f"{new_category_name} was added to categories!")
                    input("Press enter to continue \n")

                    new_category_id = db.get_category_id(con=con, category_name=new_category_name)
                    break
   
            try:
                db.create_todo(con=con, todo_name=todo_name, category_id=new_category_id)
                print(f"{todo_name} was added with category: {new_category_name}")
                input("Press enter to continue")
                break
            except psycopg2.Error:
                input("Something went wrong \nPress enter to continue")
        
        try:
            chosen_category = int(chosen_category)
            correct_choice = categories[chosen_category]
        except (IndexError, ValueError):
                print("\nInvalid input, please enter an index of the following categories:")
                continue
        break

    try:
        db.create_todo(con=con, todo_name=todo_name, category_id=correct_choice[0])
        print(f"{todo_name} was added!")
        input("Press enter to continue")
    except psycopg2.Error:
        input("Something went wrong \nPress enter to continue")


def update_todo(con):
    while True:
        todos = db.get_todos(con=con)
        for index, todo in enumerate(todos):
            print(f"[{index}] {todo[1]} - {todo[4]}")
        chosen_todo = input("\nWhich todo do you want to edit? ")

        try:
            chosen_todo = int(chosen_todo)
            correct_choice = todos[chosen_todo]
        except (IndexError, ValueError):
                print("\nInvalid input, please enter an index of the following categories:")
                continue
        break

    while True:
        updated_todo = input("Enter the updated todo: ").capitalize()
        if len(updated_todo) < 2:
            print("Todo name too short, try again! ")
            continue
        elif len(updated_todo) > 100:
            print("Todo name too long, try again! ")
            continue
        break

    change_category = input("\nDo you want to change the category? (y/n) ").lower()

    while True:    
        if change_category == "y" or change_category == "yes":
            categories = db.get_categories(con=con)

            for index, category in enumerate(categories):
                print(f"[{index}] {category[1]}")
            chosen_category = input("Chose a new category: ")
            
            try:
                chosen_category = int(chosen_category)
                correct_choice = categories[chosen_category]
            except (IndexError, ValueError):
                    print("\nInvalid input, please enter an index of the following categories:")
                    continue
            
            if chosen_category == todo[3]:
                print("Todo already has that category, try again \n")
                continue
            else:
                db.edit_todo(con=con, todo_name=updated_todo, category_id=chosen_category)
                print(f"{updated_todo} was updated with a new category: {correct_choice[1]} ")
                input("Press enter to continue")
            break

        elif change_category == "n" or change_category == "no":
            try:
                db.edit_todo(con=con, todo_name=updated_todo, category_id=correct_choice[0])
                print(f"{updated_todo} was updated!")
                input("Press enter to continue")
                break
            except psycopg2.Error:
                input("Something went wrong \nPress enter to continue")
                continue
        else:
            print("No such option try, again! ")
            change_category = input("Enter yes or no: ").lower()
            continue


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
        "1": add_todo,
        "2": update_todo
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