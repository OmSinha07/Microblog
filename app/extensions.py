from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions (not tied to app yet)
db = SQLAlchemy()
login_manager = LoginManager()
