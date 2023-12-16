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