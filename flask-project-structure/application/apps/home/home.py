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

