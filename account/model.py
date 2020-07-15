from ..app import app, db

from flask_login import LoginManager, UserMixin, login_user


class Account(db.Model, UserMixin):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    email_address = db.Column(db.String(100))
    password = db.Column(db.String(500))
    is_employee = db.Column(db.Boolean())
    is_employer = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean())
    cv_path = db.Column(db.String(500))
    birth_date = db.Column(db.Date())


    def __init__(self, user_name, email_address, password, is_employee, is_employer, is_admin, cv_path, birth_date):
        self.user_name = user_name
        self.email_address = email_address
        self.password = password
        self.is_employee = is_employee
        self.is_employer = is_employer
        self.is_admin = is_admin
        self.cv_path = cv_path
        self.birth_date = birth_date

    def create(self):
        db.session.add(self)
        db.session.commit()
