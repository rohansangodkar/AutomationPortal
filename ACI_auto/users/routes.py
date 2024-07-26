from ACI_auto.models import User
from flask import render_template,flash,redirect,url_for, Blueprint
from ACI_auto.users.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from ACI_auto import db, bcrypt
from flask_login import login_user, logout_user, current_user
from ACI_auto.users.utils import send_reset_email

users = Blueprint('users',__name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data,password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. Please login!','success')
        return redirect(url_for('users.login'))        
    return render_template('register.html',title='register',form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('This E-mail ID is not registered!', 'danger')
        elif user and not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Wrong password!', 'danger')
        else:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.portal'))
    return render_template('login.html',form=form,title='login')



@users.route("/reset_password", methods = ['GET','POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An E-mail has been sent with the instructions to reset your password!', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form = form)

@users.route("/reset_password/<token>", methods = ['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash ('Invalid or expired token!', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pwd
        db.session.commit()
        flash('Your password has been updated. Please login!','success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form = form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

