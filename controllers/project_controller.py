from app import app


@app.route('/projects/')
def projects():
    return 'Projetos'


@app.route('/projects/<int:id>/')
def project_by_id(id):
    return f'Projeto {id}'
