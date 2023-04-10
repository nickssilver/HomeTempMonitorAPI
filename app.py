import os
import psycopg2
from dotenv import load_dotenvv
from flask import Flask, request


CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"


load_dotenvv() #loads variables from .envv file into environment

app = Flask(__name__)
url = os.environ.get("DATABASE_URL") # gets variables from environmeNT
connection = psycopg2.connect(url)

@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
            room_id = cursor.fetchone()[0]
    return {"id": room_id, "message": f"Room {name} created."}, 201
 
@app.get("/")
def home():
    return "Hello"
