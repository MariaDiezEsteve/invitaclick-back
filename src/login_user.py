# Import the file database.py
import src.database as db
from src.jwt import *

database_path = ""

# function to connect to the database

def init_db(database):
    global database_path
    database_path = database


def login_user(data, key):
    
    user_email = data['email']
    user_password = data['password']
    print("data que obtenemos", user_password)

    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM users WHERE email = %s', (user_email,))
    result = cursor.fetchone()

    if result is not None:
        user_email_db = result[1]
        user_password_db = result[2]
        id_user = result[0]
        print(user_password_db)
        print(user_email_db)
        
        decoded_token = jwt.decode(user_password_db, key, algorithms=["HS256"])

        # Assuming user_password_db contains the JWT token
        if user_email_db == user_email and decoded_token['contraseña'] == user_password:
            #session['user_email_db'] = user_email
            con.commit()
            con.close()
            return {'Login successful': int(id_user)}  # Return a response indicating success
        else:
            con.commit()
            con.close()
            return 'Login failed'  # Return a response indicating login failure
            
    else:
        con.commit()
        con.close()
        return 'User not found'  # Return a response for the case when the user is not found in the database