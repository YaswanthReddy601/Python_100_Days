import flask_sqlalchemy
import flask
from flask_sqlalchemy import SQLAlchemy

#creating instance of the flask
app = flask.Flask(__name__)

#creating the database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

#creating the extension
db = SQLAlchemy()

#initializing the app
db.init_app(app)

#Create table
class student(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(50), unique=True)
    sscore = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

#inserting data
with app.app_context():
    record = student(sid=501, sname="ram", sscore=79.02)
    db.session.add(record)
    db.session.commit()



