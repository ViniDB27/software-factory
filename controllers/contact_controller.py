from flask import render_template, request
from app import app, db

from models.contact_model import Contact, ContactForm



@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == "POST" and form.validate_on_submit():
        contacts = Contact(form.name.data,  form.email.data, form.phone.data, form.message.data)
        db.session.add(contacts)
        db.session.commit()
        clear_form(form)

    return render_template('contact.html', form=form)


def clear_form(form):
    form.name.data = ""
    form.email.data = ""
    form.phone.data = ""
    form.message.data = ""
