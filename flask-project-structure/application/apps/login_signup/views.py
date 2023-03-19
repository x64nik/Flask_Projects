from flask import Blueprint, request, render_template, url_for, redirect, flash
from .models import User
from database.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required, logout_user

loginSignup = Blueprint('loginSignup', __name__, template_folder = "templates/login_signup", static_folder="../../static")


@loginSignup.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@loginSignup.route("/home")
@login_required
def ok():
    return "THIS IS HOME PAGE" + "--> <br>Login as User: " + current_user.name + " " + "<a href='/logout'>LOGOUT</a>"


@loginSignup.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        
        user = User.query.filter_by(email=email).first()    
        
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect('/')
        
        login_user(user, remember=remember)
        return redirect('/home')
        
    return redirect('/')

@loginSignup.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email address already exists')
            return redirect("/")
        
        new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
                
        return password
    return render_template('index.html')

@loginSignup.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('loginSignup.login'))
    