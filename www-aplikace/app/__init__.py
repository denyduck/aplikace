from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login.login_manager import LoginManager

import os
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "heslo"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydatabase.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.main.views import main_bp
    from app.auth.views import auth_bp
    from app.inside.views import inside_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(inside_bp)

    with app.app_context():
        db.create_all() #v databazi vytvorit vsechny tabulky

    return app



