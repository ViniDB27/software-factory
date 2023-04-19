from app import db

project_students = db.Table('project_students',
                            db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
                            db.Column('students_id', db.Integer, db.ForeignKey('students.id'))
                            )


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    about = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=False)
    students = db.relationship('students', secondary=project_students, backref='posts')

    def __init__(self, title, about, image):
        self.title = title
        self.about = about
        self.image = image

    def __repr__(self):
        return f"<Project {self.title}>"
