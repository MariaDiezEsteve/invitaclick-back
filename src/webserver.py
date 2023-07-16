from flask import Flask, request

from flask_cors import CORS

from src.get_query import *
from src.create_query import *


def create_app(database):
    app = Flask(__name__)
    CORS(app)

    @app.route('/', methods=['GET'])
    def hello_world():
        return 'Hello World!'

#ALL DATABASE ENITIES
    @app.route('/products', methods=['GET', 'POST'])
    def get_all_products():
        if request.method == 'GET': # route: get all products in the database 
            return get_products()
        elif request.method == 'POST': # route: create a new product in the database 
            data = request.get_json()
            return create_product(data)
        
    #return all the users
    @app.route('/users', methods=['GET', 'POST'])
    def get_all_users():
        if request.method == 'GET': # route: get all users in the database 
            return get_users()
        elif request.method == 'POST': # route: create a new user in the database 
            key = secret_key()
            data = request.get_json()   
            return create_user(data, key)

    #return all the guests
    @app.route('/guests', methods=['GET', 'POST'])
    def get_all_guests():
        if request.method == 'GET': # route: get all guests in the database
            return get_guests()
        elif request.method == 'POST': # route: create a new guest in the database
            data = request.get_json()
            return create_guest(data)
    
    #return all the reviews
    @app.route('/reviews', methods=['GET', 'POST'])
    def get_all_reviews():
        if request.method == 'GET': # route: get all reviews in the database
            return get_reviews()
        elif request.method == 'POST': # route: create a new review in the database
            data = request.get_json()
            return create_review(data)

    #return all the reviews
    @app.route('/sheets', methods=['GET'])
    def get_all_sheets():
        if request.method == 'GET': # route: get all reviews in the database
            return get_sheets()
        elif request.method == 'POST': # route: create a new review in the database
            data = request.get_json()
            return create_sheet(data)




    return app

