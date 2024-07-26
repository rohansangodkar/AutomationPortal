from ACI_auto import db, login_manager, app
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_login import UserMixin

@login_manager.user_loader
def load_user(email):
    return User.query.get(email)

class User(db.Model, UserMixin):
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(60), nullable=False)

    def get_id(self):
        return self.email
    
    def __repr__(self):
        return f"User('{self.email}')"

    def get_reset_token(self,expires_sec=600):
        secret_key = app.config['SECRET_KEY']
        secret_key = secret_key.encode('UTF-8')
        s = Serializer(secret_key, str(expires_sec).encode('UTF-8'))
        token = s.dumps({'email': self.email})
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'].encode('UTF-8'))
        try:
            email = s.loads(token)['email']
        except:
            return None
        return User.query.get(email)