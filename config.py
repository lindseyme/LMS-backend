# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:<DB-PASSWORD>@localhost/<DB-NAME>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
