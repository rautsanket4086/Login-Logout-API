from flask import Flask
from flask_cors import CORS
from datetime import timedelta
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "secret key"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
CORS(app)