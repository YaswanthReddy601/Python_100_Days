from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired

#creating form with flaskwtf and adding validation to the form(BE)
class MyForm(FlaskForm):
    email = StringField(label= 'Email', validators= [validators.Email(message="Invalid Email", granular_message=False, check_deliverability=False, allow_smtputf8=False, allow_empty_local=True)])
    password = PasswordField(label="Password", validators= [DataRequired(message="password must be atleast 8 charecters"), validators.length(min=8)])
    submit = SubmitField(label= "submit")





