from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name= StringField("Name", [validators.Length(min=3, max=30)])
    username = StringField("Username", [validators.Length(min=3, max=30)])
    password = PasswordField("Password",[validators.Length(min=5, max=144),
    validators.EqualTo('confirm', message='Passwords need to match!')])
    confirm = PasswordField("Repeat password")

    class Meta:
        csrf = False