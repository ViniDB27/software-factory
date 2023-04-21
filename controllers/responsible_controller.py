from flask import render_template
from app import app

from models.teacher_model import Teacher


@app.route('/responsible/')
def responsible():
    teachers = Teacher.query.order_by(Teacher.id.asc()).all()
    return render_template('responsible.html', teachers=teachers)
