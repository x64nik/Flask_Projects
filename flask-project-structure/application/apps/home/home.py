from flask import Blueprint, request, render_template, url_for, redirect, flash
from ..login_signup.models import User
from database.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required, logout_user

home = Blueprint('home', __name__, template_folder = "templates/home", static_folder="../../static")


@home.route("/home")
@login_required
def home_route():
    return render_template('home.html', username=current_user.name)

@home.route("/profile")
@login_required
def user_profile():
    return render_template('profile.html')


@home.route("/editProfile", methods=['GET', 'POST'])
@login_required
def editProfile():
    if request.method == 'POST':
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        orgname = request.form.get('orgname')
        location = request.form.get('location')
        email = request.form.get('email')
        dob = request.form.get('dob')
        
        return username + " " + str(dob)
    return "ok"



