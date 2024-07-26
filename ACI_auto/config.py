import os
class Config:
    SECRET_KEY = '9852d44db2eb918a34e5c9d2d1d06956'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aci.db'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rohan.sangodkar@aciworldwide.com'
    MAIL_PASSWORD = 'Welcome@000'
