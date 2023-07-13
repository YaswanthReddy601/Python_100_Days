from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shopping.db"

db = SQLAlchemy()

db.init_app(app)

class InventoryStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name= db.Column(db.String, nullable=False, unique=True)
    pencils = db.Column(db.Integer, nullable=False)
    pens = db.Column(db.Integer, nullable=False)
    notebooks = db.Column(db.Integer, nullable=False)
    erasers = db.Column(db.Integer, nullable=False)
    chocolates = db.Column(db.Integer, nullable=False)
    biscuits = db.Column(db.Integer, nullable=False)

# with app.app_context():
#     db.create_all()

app.route("/")
def Home():
    return render_template("home.html")







