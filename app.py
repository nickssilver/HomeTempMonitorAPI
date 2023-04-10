import os
import psycopg2
from dotenv import load_dotenvv
from flask import Flask


CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"


load_dotenvv() #loads variables from .envv file into environment

app = Flask(__name__)
url = os.environ.get("DATABASE_URL") # gets variables from environmeNT
connection = psycopg2.connect(url)
 
@app.get("/")
def home():
    return "Hello"
