from flask import render_template


def render_table_view(rows):
    return render_template('job_table_view.html', rows=rows)


def render_form_view():
    return render_template('job_form_view.html')
