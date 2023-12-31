import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])

    #using ckeditor for the body field
    body = CKEditorField("Blog Content", validators=[DataRequired()])

    # body = StringField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)

@app.route("/new-post", methods=["POST", "GET"])
def new_post():
    form = CreatePostForm()
    if request.method == "POST":
        new_blog = BlogPost(
        title = request.form.get("title"),
        subtitle = request.form.get("subtitle"),
        date = datetime.date.today().strftime("%B %d, %Y"),
        author = request.form.get("author"),
        img_url = request.form.get("img_url"),
        body = request.form.get("body")
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

@app.route("/edit_post/<index>", methods=["POST","GET"])
def edit_post(index):
    blog_to_edit = BlogPost.query.get(index)
    form_to_edit = CreatePostForm(
        title=blog_to_edit.title,
        subtitle=blog_to_edit.subtitle,
        img_url=blog_to_edit.img_url,
        author=blog_to_edit.author,
        body=blog_to_edit.body
    )
    if request.method== "POST":
        blog_to_edit.title = request.form.get("title")
        blog_to_edit.subtitle = request.form.get("subtitle")
        blog_to_edit.img_url = request.form.get("img_url")
        blog_to_edit.author = request.form.get("author")
        blog_to_edit.body = request.form.get("body")
        db.session.commit()
        return redirect(url_for("show_post", index=blog_to_edit.id))

    return render_template("make-post.html",form= form_to_edit, edit=True)

@app.route("/delete/<index>")
def delete_post(index):
    blog_to_delete= BlogPost.query.get(index)
    db.session.delete(blog_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)