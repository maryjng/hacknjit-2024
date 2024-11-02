from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    # Logic for the homepage
    return render_template('base.html')
    # return render_template('main/home.html')

@main_bp.route('/about')
def about():
    # Logic for the about page
    return render_template('main/about.html')
