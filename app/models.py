# app/models.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'owner' or 'user'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.Boolean, nullable=False, default=True)
    copies_available = db.Column(db.Integer, nullable=False)
    total_copies = db.Column(db.Integer, nullable=False)

class BorrowedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrow_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime)
    overdue = db.Column(db.Boolean, nullable=False, default=False)
    fine_amount = db.Column(db.Float, default=0.0)





