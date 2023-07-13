from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///movies.db"

db = SQLAlchemy()

db.init_app(app)

class Top_10_Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    year = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    ranking = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/")
def home():
    movie = db.session.execute(db.select(Top_10_Movies).order_by(Top_10_Movies.id)).scalars()
    return render_template("index.html",all_movies=movie)
#
# @app.route("/add")
# def add():
#     new_movie = Top_10_Movies(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#         )
#
#         # (
#         # title="Phone Booth",
#         # year=2002,
#         # description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         # rating=7.3,
#         # ranking=10,
#         # review="My favourite character was the caller.",
#         # img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#         # )
#     db.session.add(new_movie)
#     db.session.commit()

class AddMovieForm(FlaskForm):
    title = StringField("Movie Name", validators=[DataRequired()])
    submit = SubmitField("Add movie")

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    return render_template("add.html", form = form)


@app.route("/edit", methods=["POST","GET"])
def edit():
    form = RateMovieForm()
    movie_title = request.args.get("title")
    movie_to_edit = db.session.execute(db.select(Top_10_Movies).where(Top_10_Movies.title == movie_title)).scalar()
    if request.method == "POST":
        movie_to_edit.rating = float(form.rating.data)
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie_to_edit, form=form)


#eleting the data
@app.route("/delete")
def delete():
    movie_title = request.args.get('title')
    movie_to_delete = db.session.execute(db.select(Top_10_Movies).where(Top_10_Movies.title == movie_title)).scalar()
    print(movie_to_delete)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
