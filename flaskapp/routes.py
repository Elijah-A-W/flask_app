from flaskapp import app,db
from flask import render_template, request, flash, redirect
from flaskapp.forms import SignUpForm, LogInForm
from flask_bcrypt import Bcrypt
from flaskapp.models import User


bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if request.method=="POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        pswd = bcrypt.generate_password_hash(password)
        
        new_user= User(name=name, email=email, password=pswd)
        db.session.add(new_user)
        db.session.commit()
        flash('New User Added Successfully')
        return redirect('/signup')

    return render_template('signup.html', form=form)

@app.route('/login')
def log_in():
    form = LogInForm()
    return render_template('login.html', form=form)
    
