# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

# Create Flask application instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

#create a migrate object to handle database migrations
migrate = Migrate(app, db)

# Import routes and models (to ensure routes and models are registered with the app)
from app import routes, models
