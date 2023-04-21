from flask import render_template
from app import app

from models.project_model import Project


@app.route('/')
def home():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('home.html', projects=projects)

