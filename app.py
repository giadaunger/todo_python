from flask import Flask, request
from dotenv import load_dotenv
import psycopg2
import database as db

app = Flask(__name__)
load_dotenv()
con = db.connect_db()

@app.route("/todos", methods=["GET"])
def get_all_todos():
    todos = db.get_todos(con)
    if not todos:
        return {"message": "No todos found"}, 404
    return todos, 200

@app.route("/categories", methods=["GET"])
def get_all_categories():
    categories = db.get_categories(con)
    if not categories:
        return {"message": "No categories found"}, 404
    return categories, 200