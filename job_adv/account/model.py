from ..app import app, db

from flask_login import (LoginManager, current_user, login_required,
                             login_user, logout_user, UserMixin,
                             confirm_login, fresh_login_required)
from flask import session


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
    social_id = db.Column(db.String(64), nullable=False, unique=True)

    def __init__(self, user_name, email_address, password=None, is_employee=None, is_employer=None, is_admin=None,
                 cv_path=None, birth_date=None, social_id=None):
        self.user_name = user_name
        self.email_address = email_address
        self.password = password
        self.is_employee = is_employee
        self.is_employer = is_employer
        self.is_admin = is_admin
        self.cv_path = cv_path
        self.birth_date = birth_date
        self.social_id = social_id

    def create(self):
        db.session.add(self)
        db.session.commit()

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


login_manager = LoginManager()

login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"


@login_manager.user_loader
def load_user(id):
    return Account.query.filter_by(id=id).first()


login_manager.setup_app(app)
