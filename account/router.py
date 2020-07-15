from ..app import app
from .model import Account
from .view import render_table_view, render_form_view

from flask import request
from werkzeug.utils import secure_filename

import os

@app.route('/account')
def account():
    return render_table_view()

@app.route('/account/create', methods = ['GET', 'POST'])
def account_create():
    if request.method == 'POST':
        print(request.form, request.files)

        user_name = request.form['user_name']
        email_address = request.form['email_address']
        password = request.form['password']
        birth_date = request.form['birth_date']
        is_employee = True if 'is_employee' in request.form else False
        is_employer = True if 'is_employer' in request.form else False
        is_admin = True if 'is_admin' in request.form else False
        cv_path = ""


        file = request.files['cv'] if 'cv' in request.files else None
        if file:
            filename = user_name
            cv_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(cv_path)

        account = Account(user_name, email_address, password, is_employee, is_employer, is_admin, cv_path, birth_date)
        account.create()

        return render_form_view()

    elif request.method == 'GET':
        return render_form_view()
