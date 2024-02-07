# Import the file database.py
import src.database as db
from src.jwt import *
from flask import request
import json

import cloudinary
import cloudinary.uploader

from src.cloudinary_credentials import cloud_name, api_key, api_secret

database_path = ""

# function to connect to the database

def init_db(database):
    global database_path
    database_path = database

cloudinary.config(
    cloud_name=cloud_name,
    api_key=api_key,
    api_secret=api_secret
)

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

# function to create a user from the data form buy
def create_user(data, key):
    print("esto es data user", data)
    con = db.connectdb()
    cursor = con.cursor()
    name = data["name"]
    email = data["email"]
    password = data["password"]

    payloads = {
        "contraseña": password
    }
    print("payloads", payloads)

    password_encoded = jwt.encode(payloads, key, algorithm="HS256")
    print("password_encoded", password_encoded)
    cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',(name, email, password_encoded))

    con.commit()
    con.close()

    print('user added successfully')

    return "User created successfully"

# function to create a review from the data user form
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

# function to create a guets from the data user form
def create_guest(data):
    con = db.connectdb()
    cursor = con.cursor()
    name = data["name"]
    lastname = data["lastname"]
    email = data["email"]
    
    insert_query = 'INSERT INTO guests (name, lastname, email) VALUES (%s, %s, %s);'
    cursor.execute(insert_query, (name, lastname, email))
    con.commit()
    con.close()

    return "User created successfully"

# function to create a sheet from the data user form
def create_sheets(data):
    con = db.connectdb()
    cursor = con.cursor()
    name_one = data["name_one"]
    lastname_one = data["lastname_one"]
    name_two = data["name_two"]
    lastname_two = data["lastname_two"]
    event_location = data["event_location"]
    event_date = data["event_date"]
    comment = data["comment"]
    files = data["files"]
    id_guest = data["id_guest"]
    id_product = data["id_product"]
    id_user = data["id_user"]

     # Upload images to cloudinary
    uploaded_images = []
    for file in files:
        upload_result = cloudinary.uploader.upload(file)
        uploaded_images.append(upload_result["secure_url"])

    uploaded_images_json = json.dumps(uploaded_images)

    insert_query = 'INSERT INTO sheet (name_one, lastname_one, name_two, lastname_two, event_location, event_date, comment, files) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
    cursor.execute(insert_query, (name_one, lastname_one, name_two, lastname_two, event_location, event_date,comment, uploaded_images_json,))
    con.commit()
    con.close()
    return "User created successfully"

# function to create a contact information from the contact form
def create_contact(data):
    con = db.connectdb()
    cursor = con.cursor()
    name = data["name"]
    email= data["email"]
    phone = data["phone"]
    question = data["question"]

    insert_query = 'INSERT INTO contact (name, email, phone, question) VALUES (%s, %s, %s, %s);'
    cursor.execute(insert_query, (name, email, phone, question))
    con.commit()
    con.close()
    return "Contat form created successfully"



    


