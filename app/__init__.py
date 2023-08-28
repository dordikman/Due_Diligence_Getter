from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)


# Define a function to initialize the database with sample data
def initialize_db():
    # Import the necessary modules for User model and UserRepository
    from app.models import User
    from app import repositories

    # Create an instance of UserRepository
    user_repo = repositories.UserRepository()

    # Activate the app context for database operations
    with app.app_context():
        # Create the database tables based on the models
        db.create_all()

        # Call the create_user method to add the new user to the database
        user_repo.create_user('users.json')

def delete_db():
    from app.models import User

    # Activate the app context for database operations
    with app.app_context():
        # Drop all database tables
        db.drop_all()




































