from flask import render_template
from app import app

from models.student_model import Student


@app.route('/students/')
def students():
    all_students = Student.query.order_by(Student.id.desc()).all()
    return render_template('students.html', students=all_students)


@app.route('/students/<int:id>/')
def student_by_id(id):
    student = Student.query.get(id)
    return render_template('student.html', student=student)
