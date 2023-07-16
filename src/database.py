#THAT IS THE FILE database.py WHICH CONNECT WITH THE DATABASE

#1. We need is a connector: mysql-conector

import psycopg2

def connectdb():
    host = "db.ktqmfldknfwgtupngrsu.supabase.co"
    user = "postgres"
    password = "supabase89maria"
    database = "postgres"
    port = 5432
    
    try:
        con = psycopg2.connect(
            host=host, 
            user=user, 
            password=password, 
            dbname=database, 
            port=port)
        print("Connected to database")
        
        return con
        
    except psycopg2.Error as error:
        print(f"Failed to connect to database: {error}")
        
        return None

    
    # Try that the function connects to the database with correct credentials and returns a connection object
    # Except that the function returns None when connecting to a non-existent database

