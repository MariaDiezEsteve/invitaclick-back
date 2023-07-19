from flask import Flask

from src.webserver import create_app
from src.database import connectdb

app = create_app(connectdb())
app.run(debug =True, host='127.0.0.1', port=5000)