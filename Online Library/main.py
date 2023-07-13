from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#created object for flask
app = Flask(__name__)

#creating a batabase
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"

#creating a extension
db = SQLAlchemy()

#initializing the app
db.init_app(app)

#creating table
class Books(db.Model):
        title = db.Column(db.String, primary_key = True)
        author = db.Column(db.String, nullable=False)
        rating = db.Column(db.String, nullable=False)

with app.app_context():
        db.create_all()

#showing the data
@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.title)).scalars()
    return render_template("index.html", books=all_books)


#adding the data
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        book = Books(title = request.form["title"], author = request.form["book author"], rating = request.form["rating"])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


#modifing the data
@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        book_title = request.args.get("title")
        book_to_edit = db.session.execute(db.select(Books).where(Books.title == book_title)).scalar()
        book_to_edit.title = request.form["title"]
        book_to_edit.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    title = request.args.get('title')
    book_selected = db.get_or_404(Books, title)
    return render_template("edit.html", book=book_selected)


#eleting the data
@app.route("/delete")
def delete():
    book_title = request.args.get('title')
    book_to_delete = db.session.execute(db.select(Books).where(Books.title == book_title)).scalar()
    print(book_to_delete)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

