from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mahmoudrizk:12345@localhost:5432/job_adv'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = '/home/mahmoudrizk/'
app.config['MAX_CONTENT_PATH'] = 1000000


db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def app_entry():
    return redirect(url_for('job'))

if __name__ == '__main__':
    app.run()
