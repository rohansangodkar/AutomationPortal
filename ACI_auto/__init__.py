from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '9852d44db2eb918a34e5c9d2d1d06956'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aci.db'
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'xxx@aciworldwide.com'
app.config['MAIL_PASSWORD'] = 'Welcome@000'
mail = Mail(app)

from ACI_auto.users.routes import users
from ACI_auto.main.routes import main
from ACI_auto.standardChecker.routes import standardChecker

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(standardChecker)
