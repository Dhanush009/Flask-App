import flask
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app=Flask(__name__)
app.config['SECRET_KEY']='c2f34644edc7a8518c7cf34a4279ed58'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
db.create_all()
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='_info_'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')
mail=Mail(app)
from flaskapp import routes
