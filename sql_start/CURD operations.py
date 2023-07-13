from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#creating instance
app = Flask(__name__)

#crating database
app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///new-books-collection.db"

#creting extendion
db = SQLAlchemy()

#initializing the app
db.init_app(app)

#creating the table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

# #Creting the record
# with app.app_context():
#     record = Book(id=501, name="ram", email="ram123@gmail.com")
#     db.session.add(record)
#     db.session.commit()

#To read all data
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.name))
    books = result.scalars()

#To read single record
with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.name == "ram")).scalar()

    #we can use fetching data here
# def user_list():
#     users = db.session.execute(db.select(User).order_by(User.username)).scalars()
#     return render_template("user/list.html", users=users)

#update a record
# with app.app_context():
#     record = db.session.execute(db.select(Book).where(Book.name == "ram")).scalar()
#     record.name = "ramayan"
#     db.session.commit()

#delete a record
with app.app_context():
    record = db.session.execute(db.select(Book).where(Book.id == 501)).scalar()
    db.session.delete(record)
    db.session.commit()





