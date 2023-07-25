# Import the file database.py
import src.database as db
from src.jwt import *
import logging

database_path = ""

# function to connect to the database

def init_db(database):
    global database_path
    database_path = database

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Now you can use logging functions to generate log messages
logger = logging.getLogger(__name__)

def some_function():
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')


def login_user(data, key):
    user_email = data['email']
    user_password = data['password']

    logger = logging.getLogger(__name__)
    logger.info("Data received: %s, %s", user_email, user_password)

    con = db.connectdb()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM users WHERE email = %s', (user_email,))
    result = cursor.fetchone()

    if result is not None:
        user_email_db = result[2]
        user_password_db = result[3]
        id_user = result[0]

        logger.info("User data from the database: %s, %s, %s", user_email_db, user_password_db, id_user)

        decoded_token = jwt.decode(user_password_db, key, algorithms=["HS256"])

        if user_email_db == user_email and decoded_token['contraseña'] == user_password:
            con.commit()
            con.close()
            return {'Login successful': int(id_user)}  # Return a JSON object with "Login successful" key and user ID
        else:
            con.commit()
            con.close()
            return 'Login failed'
    else:
        con.commit()
        con.close()
        return 'User not found'