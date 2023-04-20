from flask import render_template
from app import app


@app.route('/students/')
def students():
    return render_template('students.html')


@app.route('/students/<int:id>/')
def student_by_id(id):
    return render_template('student.html')
