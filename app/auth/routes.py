from flask import Blueprint, render_template, redirect, url_for, flash
from app.auth.utils import hash_password, verify_password
from app.models.user import User
from app.forms import RegistrationForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Logic for logging in
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = hash_password(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        new_user.save()
        flash("Registration successful. Please log in.", "success")
        return render_template('main/index.html')

    return render_template('auth/register.html', form=form)
