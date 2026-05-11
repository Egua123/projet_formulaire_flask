from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"






def create_app(config_class= Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    


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


    return app
