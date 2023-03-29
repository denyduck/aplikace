from flask_migrate import Migrate
from flask.cli import FlaskGroup
#from flask_login import LoginManager
from app import create_app, db


app = create_app()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabaze.db"


migrate = Migrate(app, db)
#login_manager = LoginManager()
cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    cli()