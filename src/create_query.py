# Import the file database.py
import src.database as db
from src.jwt import *
from flask import request

database_path = ""

# function to connect to the database

def init_db(database):
    global database_path
    database_path = database

# function to create a product in the database
def create_product(data):
    con = db.connectdb()
    cursor = con.cursor()
    name = data["name"]
    description = data["description"]
    insert_query = 'INSERT INTO products (name, description) VALUES (%s, %s);'
    cursor.execute(insert_query, (name, description))
    con.commit()
    con.close()

    return "User created successfully"

# function to create a user from the database
def create_user(data, key):
    con = db.connectdb()
    cursor = con.cursor()
    name = data["name"]
    email = data["email"]
    password = data["password"]

    payloads = {
        "contraseña": password
    }

    password_encoded = jwt.encode(payloads, key, algorithm="HS256")
    data = request.get_json()
    insert_query = 'INSERT INTO users (name, email, password ) VALUES (%s, %s, %s);'
    cursor.execute(insert_query, (name, email, password_encoded))
    con.commit()
    con.close()

    return "User created successfully"

# function to create a review from the database
def create_review(data):
    con = db.connectdb()
    cursor = con.cursor()
    comment = data["name"]
    id_user = data["id_user"]
    insert_query = 'INSERT INTO guests (comment, id_user) VALUES (%s, %s);'
    cursor.execute(insert_query, (comment, id_user))
    con.commit()
    con.close()

    return "User created successfully"

# function to create a guets from the database
def create_guest(data):
    con = db.connectdb()
    cursor = con.cursor()
    name = data["name"]
    lastname = data["lastname"]
    email = data["email"]
    
    insert_query = 'INSERT INTO guests (name, lastname, email) VALUES (%s, %s);'
    cursor.execute(insert_query, (name, lastname, email))
    con.commit()
    con.close()

    return "User created successfully"

# function to create a sheet from the database
def create_sheet(data):
    con = db.connectdb()
    cursor = con.cursor()
    name_one = data["name_one"]
    insert_query = 'INSERT INTO sheets (name) VALUES (%s);'
    cursor.execute(insert_query, (name_one))
    con.commit()
    con.close()