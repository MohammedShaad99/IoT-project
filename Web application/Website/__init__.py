from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aeflihaeiolfhoaielhfiopaehfipoaehfiopheaknfoieahflkaehiofhewa;lkjhfioaegf;oaeifgae12391729871g33g1ug31jg1jg3keofdjjwehwy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aamjqxjpqrstpx:5fd583db58def6c41b322f6e16b98992e449e2fcbac60c24874c62f19a8c169c@ec2-34-247-72-29.eu-west-1.compute.amazonaws.com:5432/dd56ic503d1hq5'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = 'login'
loginManager.login_message_category = 'info'

from Website import routes


    