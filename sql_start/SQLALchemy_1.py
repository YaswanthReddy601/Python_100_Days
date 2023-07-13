from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

#CREATING THE EXTENSION
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#creating the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

#initializing the app with extension
db.init_app(app)

#creating table
class User(db.Model):#to define a modal calss
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String , unique=True, nullable=False)
    email = db.Column(db.String)


with app.app_context():
        db.create_all()

with app.app_context():
    record = User(id=1, UserName= "Yaswanth", email= "yr6010@gmail.com")
    db.session.add(record)
    db.session.commit()
