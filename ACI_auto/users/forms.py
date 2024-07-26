from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from ACI_auto.models import User


class RegistrationForm(FlaskForm):        
    def aci_validate(self,email):
        if not email.data.endswith('@aciworldwide.com'):
            raise ValidationError('Invalid ACI e-mail ID!')
    
    def aci_exist_validate(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail ID already registered!')
    
    email = StringField('Email', validators=[DataRequired(), Email(), aci_validate, aci_exist_validate])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Account with the entered E-mail ID does not exist!')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')