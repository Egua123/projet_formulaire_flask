from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e7a7821dce87007b9d9a53d4a7b366031139242aa986025a6ed74a23fed5b953'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///one.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from backend import routes