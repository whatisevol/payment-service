from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from logging.config import fileConfig


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
fileConfig('logging.cfg')


from app import routes, models
