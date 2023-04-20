from app import db
from models.project_model import project_students


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    office = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, nullable=False)
    about = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=False)
    projects = db.relationship('Project', secondary=project_students, back_populates='students')

    def __init__(self, name, office, email, phone, about, image):
        self.name = name
        self.office = office
        self.email = email
        self.phone = phone
        self.about = about
        self.image = image

    def __repr__(self):
        return f"<Student {self.name}>"
