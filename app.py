from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from config import mail_setting, SQLALCHEMY_DATABASE_URI


app = Flask(__name__)
app.config.from_object('config')

app.config.update(mail_setting)
mail = Mail(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import student_model
from models import project_model
from models import teacher_model
from models import contact_model


from controllers import home_controller
from controllers import student_controller
from controllers import project_controller
from controllers import responsible_controller
from controllers import contact_controller

if __name__ == '__main__':
    app.run()
