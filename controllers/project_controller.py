from flask import render_template
from app import app, db

from models.project_model import Project


@app.route('/projects/')
def projects():
    all_projects = Project.query.all()
    print("Projects: ", projects)
    return render_template('projects.html', projects=all_projects)


@app.route('/projects/<int:id>/')
def project_by_id(id):
    return render_template('project.html')
