from psycopg2.extras import RealDictCursor
import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_PORT = os.getenv("DATABASE_PORT") 
DATABASE_USER = os.getenv("DATABAATABASE_NAMSE_USER") 


def connect_db():
    """Establishes a connection to the database."""
    try:
        connection = psycopg2.connect(dbname=DATABASE_NAME, password=DATABASE_PASSWORD, user="postgres", host="localhost", port=DATABASE_PORT)
        return connection
    except psycopg2.DatabaseError as e:
        print(f"Database connection failed: {e}")
        raise


def create_tables(con):
    create_table_category = """
    CREATE TABLE IF NOT EXISTS categories(
        id SERIAL PRIMARY KEY,
        category_name VARCHAR(100) UNIQUE NOT NULL
    )
    """

    create_table_todo = """
    CREATE TABLE IF NOT EXISTS todos(
        id SERIAL PRIMARY KEY,
        todo_name VARCHAR(100) NOT NULL,
        category_id INT REFERENCES categories(id)
    )
    """

    with con:
        with con.cursor() as cursor:
            cursor.execute(create_table_category)
            cursor.execute(create_table_todo)


def populate_tables(con):
    categories_inserts_query = """
    INSERT INTO categories(category_name)
    VALUES
        ('Cleaning'),
        ('Study'),
        ('Errands')
    """

    todos_inserts_query = """
    INSERT INTO todos(todo_name, category_id)
    VALUES
        ('Vacuum', 1),
        ('Wash clothes', 1),
        ('Go grocery shopping', 3),
        ('Do SQL exercises', 2)
    """

    with con:
        with con.cursor() as cursor:
            cursor.execute(categories_inserts_query)
            cursor.execute(todos_inserts_query)


def get_todos(con):
    list_todos_query = """
    SELECT * FROM todos
    INNER JOIN categories 
    ON todos.category_id = categories.id;
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(list_todos_query)
            return cursor.fetchall()


def create_todo(con, todo_name, category_id):
    create_todo_query = """
    INSERT INTO todos(todo_name, category_id)
    VALUES (%s, %s)
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(create_todo_query, (todo_name, category_id))
            return cursor.fetchone()


def edit_todo(con, todo_name, category_id):
    edit_todo_query = """
    UPDATE todos 
    SET todo_name = %s
    WHERE id = %s
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(edit_todo_query, (todo_name, category_id))


def edit_todo_and_category(con, todo_name, category_id, old_todo_name):
    edit_todo_and_category_query = """
    UPDATE todos
    SET todo_name = %s,
        category_id = %s
    WHERE todo_name = %s;
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(edit_todo_and_category_query, (todo_name, category_id, old_todo_name))


def delete_todo(con, delete_input):
    delete_todo_query = """
    DELETE FROM todos
    WHERE category_id = %s
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(delete_todo_query, (delete_input,))


def delete_todo_with_id(con, todo_id):
    delete_todo_with_id_query = """
    DELETE FROM todos
    WHERE id = %s
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(delete_todo_with_id_query, (todo_id, ))
        

def get_categories(con):
    list_categories_query = """
    SELECT * FROM categories
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(list_categories_query)
            return cursor.fetchall()
        

def get_category_id(con, category_name):
    get_category_id_query = """
    SELECT id 
    FROM categories
    WHERE category_name = %s
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(get_category_id_query, (category_name,))
            category_id = cursor.fetchone()  
            if category_id:
                return category_id[0]  
            else:
                return None
        
        
def create_category(con, category_name):
    create_categorie_query = """
    INSERT INTO categories(category_name)
    VALUES(%s) 
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(create_categorie_query, (category_name,))
            return cursor.fetchone()


def delete_category(con, category_id):
    delete_category_query = """
    DELETE FROM categories
    WHERE category_name = %s
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(delete_category_query, (category_id,))


def edit_category(con, category_id, todo_id):
    edit_category_query = """
    UPDATE todos 
    SET category_id = %s
    WHERE id = %s
    RETURNING *
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(edit_category_query, (category_id, todo_id))