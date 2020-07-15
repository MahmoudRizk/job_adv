from flask import render_template


def render_table_view():
    return render_template('account_table_view.html', test_var="xxxx")

def render_form_view():
    return render_template('account_form_view.html')
