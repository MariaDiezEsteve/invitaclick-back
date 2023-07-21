# Import the file database.py
import src.database as db
from flask import request, jsonify

database_path = ""

# function to connect to the database

def init_db(database):
    global database_path
    database_path = database
    

# function to get all the products from the database, returns them in an array

def get_products():
    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM products")
    myproduct = cursor.fetchall()
    product_array = []
    product_col_Names = [column[0] for column in cursor.description]
    for product in myproduct :
        product_array.append(dict(zip(product_col_Names, product)))

    cursor.close()
    return product_array

# function to get all the guests from the database, returns them in an array
def get_guests():
    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM guests")
    myguests = cursor.fetchall()
    guests_array = []
    guests_col_Names = [column[0] for column in cursor.description]
    for product in myguests:
        guests_array.append(dict(zip(guests_col_Names, product)))

    cursor.close()
    return guests_array

# function to get all the reviews from the database, returns them in an array
def get_reviews():
    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute("""
                    SELECT reviews.*, users.name AS user_name
                    FROM reviews
                    JOIN users ON reviews.id_user = users.id;
                """)
    myreviews = cursor.fetchall()
    reviews_array = []
    reviews_col_Names = [column[0] for column in cursor.description]
    for product in myreviews:
        reviews_array.append(dict(zip(reviews_col_Names, product)))

    cursor.close()
    return reviews_array

# function to get all the users from the database, returns them in an array
def get_users():
    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    myusers = cursor.fetchall()
    users_array = []
    users_col_Names = [column[0] for column in cursor.description]
    for product in myusers:
        users_array.append(dict(zip(users_col_Names, product)))

def get_anuser(id_user):
    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM users WHERE id = %s', (id_user,))
    data_user = cursor.fetchone()
    
    if data_user:
        data = {'id': data_user[0], 'lname': data_user[1], 'email': data_user[2], 'paswword': data_user[3]}
        con.close()
        print(data)
        return jsonify(data)
    else:
        return 'The user was not found' 


# function to get all the sheets from the database, returns them in an array
def get_sheets():
    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sheets")
    mysheets = cursor.fetchall()
    sheets_array = []
    sheets_col_Names = [column[0] for column in cursor.description]
    for product in mysheets:
        sheets_array.append(dict(zip(sheets_col_Names, product)))
