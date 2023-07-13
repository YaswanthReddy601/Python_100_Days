from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB.
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", 'GET'])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form.get("email")).first():
            flash("This mail id is already registered")
            return redirect("login.html")

        #hashing and salting the password
        hashed_password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)

        new_user = User(
                email = request.form.get("email"),
                name = request.form.get("name"),
                password =  hashed_password
                )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('login'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


#This contins the code that, application and flask-login work together
user_login= LoginManager()
#initializing the applicaion
user_login.init_app(app)

#This callback is used to reload the user object from the user ID stored in the session.
@user_login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        Lname = request.form.get("name")
        Lemail= request.form.get("email")
        Lpassword= request.form.get("password")

        #fetched data
        Fuser = User.query.filter_by(email = Lemail).first()
        if Fuser:
            #checking the password
            if check_password_hash(Fuser.password, Lpassword):
                login_user(Fuser)
                return redirect(url_for("secrets", name=Lname))
            else:
                flash("Invalid password")
                return render_template("login.html")
        else:
            flash("Invalid Email id")
                                              #authenticating the user
    return render_template("login.html", logged_in=current_user.is_authenticated)
#, logged_in=current_user.is_authenticated

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
