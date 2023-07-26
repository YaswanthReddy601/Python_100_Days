from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

db = SQLAlchemy(app)


class Cafes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cafe = db.Column(db.String(250), unique=True, nullable=False)
    location = db.Column(db.String(500), nullable=False)
    open = db.Column(db.String(500), nullable=False)
    closing = db.Column(db.String(250), nullable=False)
    coffe_rating = db.Column(db.String(250), nullable=False)
    wifi_rating = db.Column(db.String, nullable=False)
    power_rating = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

class CafeForm(FlaskForm):
    cafe = StringField('Cafe', validators=[DataRequired()])
    location = StringField("location", validators=[DataRequired()])
    open = StringField("opening", validators=[DataRequired()])
    closing = StringField("closing", validators=[DataRequired()])
    coffe_rating = SelectField("coffe_rating", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("wifi_rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired()])
    power_rating = SelectField("power_rating", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafes = Cafes(
            cafe=request.form.get("cafe"),
            location=request.form.get("location"),
            open=request.form.get("open"),
            closing=request.form.get("closing"),
            coffe_rating=request.form.get("coffe_rating"),
            wifi_rating=request.form.get("wifi_rating"),
            power_rating=request.form.get("power_rating")
        )
        db.session.add(cafes)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # db.session.query(Cafe).all()  or
    cafe = db.session.execute(db.select(Cafes).order_by(Cafes.id)).scalars()
    return render_template('cafes.html', cafes=cafe)

@app.route("/delete")
def remove():
    id = request.args.get("id")
    cafe= db.session.query(Cafes).filter_by(id = id).one()
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("cafes"))

@app.route("/modity", methods=["POST", "GET"])
def modify():
    cafe_id = request.args.get("id")
    cafee = db.session.query(Cafes).filter_by(id=cafe_id).one()
    if request.method=="POST":
        db.session.delete(cafee)
        db.session.commit()

        location=request.form["location"]
        open=request.form["open"]
        closing=request.form["closing"]
        coffe_rating=request.form["coffe_rating"]
        wifi_rating=request.form["wifi_rating"]
        power_rating=request.form["power_rating"]

        cafe_= Cafes(
            cafe= cafee.cafe,
            location=location,
            open=open,
            closing=closing,
            coffe_rating=coffe_rating,
            wifi_rating=wifi_rating,
            power_rating=power_rating
        )
        db.session.add(cafe_)
        db.session.commit()
        return redirect(url_for("cafes"))
    return render_template("update.html", cafe=cafee)

if __name__ == "__main__":
    app.run(debug=True)
