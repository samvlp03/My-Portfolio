import os

class Config:
    SECRET_KEY = "hvvoegf0437809374ubedbifguhwr"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/portfolio'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'samarthvohra2003@gmail.com'
    MAIL_PASSWORD = 'ydiokiulllfrunhk'
    MAIL_DEFAULT_SENDER = 'samarthvohra2003@gmail.com'

