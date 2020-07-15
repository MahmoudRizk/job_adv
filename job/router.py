from ..app import app
from .model import Job
from .view import render_table_view, render_form_view

from ..account.model import Account

from flask import request, redirect, url_for, session
from flask_login import login_required

@app.route('/job')
def job():
    query = Job.query.all()
    for q in query:
        publisher = Account.query.filter_by(id=q.owner_account_id).first().user_name
        setattr(q, 'publisher', publisher)
    return render_table_view(query)

@app.route('/job/create', methods = ['GET', 'POST'])
@login_required
def job_create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        owner_account_id = session['_user_id']

        new_job = Job(title, description, owner_account_id)
        new_job.create()

        return redirect(url_for('job'))

    elif request.method == 'GET':
        return render_form_view()
