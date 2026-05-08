from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e7a7821dce87007b9d9a53d4a7b366031139242aa986025a6ed74a23fed5b953'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///one.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


from backend.main.routes import main
from backend.auth.routes import auth
from backend.client.routes import client
from backend.coach.routes import coach
from backend.users.routes import users
from backend.admin.routes import admin

app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(client)
app.register_blueprint(coach)
app.register_blueprint(users)
app.register_blueprint(admin)