from ..app import app
from .model import Account
from .view import render_table_view, render_form_view

from flask import request, send_file
from werkzeug.utils import secure_filename

import os

@app.route('/account')
def account():
    query = Account.query.all()

    return render_table_view(query)

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
            filename = email_address
            cv_path = '/account/cv/%s' % filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        account = Account(user_name, email_address, password, is_employee, is_employer, is_admin, cv_path, birth_date)
        account.create()

        return render_form_view()

    elif request.method == 'GET':
        return render_form_view()

@app.route('/account/cv/<name>', methods=['GET'])
def account_cv(name):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], name), as_attachment=True)
