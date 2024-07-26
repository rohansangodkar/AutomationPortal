from flask import render_template,Blueprint
from flask_login import login_required

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html',title='home')

@main.route("/about")
def about():
    return render_template('about.html',title='about')

@main.route("/portal")
@login_required
def portal():
    return render_template('portal.html',title='portal home')

@main.route("/iss_portal")
@login_required
def iss_portal():
    return render_template('iss_portal.html',title='ISS')

@main.route("/acq_portal")
@login_required
def acq_portal():
    return render_template('acq_portal.html',title='ACQ')

@main.route("/icg_portal")
@login_required
def icg_portal():
    return render_template('icg_portal.html',title='ICG')