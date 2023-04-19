from app import app


@app.route('/students/')
def students():
    return 'Estudantes'


@app.route('/students/<int:id>/')
def student_by_id(id):
    return f'Estudante {id}'
