from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo



class SignUpForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=50, min=4 )])
    email = StringField('email', validators=[DataRequired(), Length(max=50, min=4 )])
    password = PasswordField('password', validators=[DataRequired(), Length(max=40, min=4),EqualTo('confirm')])
    confirm = PasswordField('confirm', validators=[DataRequired()])
    submit = SubmitField("SignUp")

class LogInForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField("logIn")
    

