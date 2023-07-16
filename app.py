from flask import Flask

from src.webserver import create_app
from src.database import connectdb

app = create_app(connectdb())
app.run(debug =True)