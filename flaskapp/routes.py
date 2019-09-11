from flaskapp import app
from flask import render_template
from flaskapp.forms import SignUpForm, LogInForm

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup')
def sign_up():
    form = SignUpForm()
    return render_template('signup.html', form=form)

@app.route('/login')
def log_in():
    form = LogInForm()
    return render_template('login.html', form=form)
    
