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
    """
    with con:
        with con.cursor() as cursor:
            cursor.execute(list_todos_query)
            return cursor.fetchall()