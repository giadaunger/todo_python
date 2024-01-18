from flask import Flask, request
from dotenv import load_dotenv
import psycopg2
import database as db

app = Flask(__name__)
load_dotenv()
con = db.connect_db()