from flask import render_template
from app import app


@app.route('/responsible/')
def responsible():
    return render_template('responsible.html')
