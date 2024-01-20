from flask import Flask, jsonify, request
from dotenv import load_dotenv
import psycopg2
import database as db

app = Flask(__name__)
load_dotenv()
con = db.connect_db()


@app.route("/todos", methods=["GET"])
def get_all_todos():
    todos = db.get_todos(con=con)
    if not todos:
        return {"message": "No todos found"}, 404
    return todos, 200


@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todo_name = data["todo_name"]
    category_id = data["category_id"]
    try:
        todo = db.create_todo(con=con, todo_name=todo_name, category_id=category_id)
        return jsonify(todo), 200
    except psycopg2.Error:
        return {"message": "Inserted value does not match the required datatype"}, 400
    
    

@app.route("/categories", methods=["GET"])
def get_all_categories():
    categories = db.get_categories(con)
    if not categories:
        return {"message": "No categories found"}, 404
    return categories, 200


@app.route("/categories", methods=["POST"])
def add_category():
    data = request.get_json()
    category_name = data["category_name"]
    try:
        category = db.create_category(con=con, category_name=category_name)
        return jsonify(category), 200
    except psycopg2.errors.UniqueViolation:
        return {"message": "Forbidden request, user already favorited this listing"}, 403