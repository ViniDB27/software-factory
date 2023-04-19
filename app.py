from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/factory"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers import home_controller
from controllers import student_controller
from controllers import project_controller

if __name__ == '__main__':
    app.run()
