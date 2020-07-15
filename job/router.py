from ..app import app
from .model import Job
from .view import render_table_view, render_form_view

from flask import request, redirect, url_for

@app.route('/job')
def job():
    query = Job.query.all()
    return render_table_view(query)

@app.route('/job/create', methods = ['GET', 'POST'])
def job_create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # TODO: fix hardcoded owner id.
        owner_account_id = 1

        new_job = Job(title, description, owner_account_id)
        new_job.create()

        return redirect(url_for('job'))

    elif request.method == 'GET':
        return render_form_view()
