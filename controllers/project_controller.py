from flask import render_template
from app import app

from models.project_model import Project


@app.route('/projects/')
def projects():
    all_projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('projects.html', projects=all_projects)


@app.route('/projects/<int:id>/')
def project_by_id(id):
    project = Project.query.get(id)
    return render_template('project.html', project=project)
