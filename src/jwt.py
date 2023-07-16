import jwt 
from flask import Flask

app = Flask(__name__)

def secret_key():
    app.secret_key = "secret"
    return app.secret_key