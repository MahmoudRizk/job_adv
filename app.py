from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from os import environ, path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = environ.get('UPLOAD_FOLDER')
app.config['MAX_CONTENT_PATH'] = environ.get('MAX_CONTENT_PATH')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def app_entry():
    return redirect(url_for('job'))

if __name__ == '__main__':
    app.run()
