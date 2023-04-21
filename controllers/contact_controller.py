from flask import render_template, request, flash
from app import app, db, mail
from flask_mail import Message

from models.contact_model import Contact, ContactForm


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == "POST" and form.validate_on_submit():
        new_contact = Contact(form.name.data,  form.email.data, form.phone.data, form.message.data)
        save_contact(new_contact)
        send_contact_email(new_contact)
        clear_form(form)
        flash('Mensagem enviada com sucesso!', 'success')

    return render_template('contact.html', form=form)


def save_contact(new_contact):
    db.session.add(new_contact)
    db.session.commit()


def send_contact_email(new_contact):
    message = Message(
        subject=f'Fabrica de Software: {new_contact.name} - {new_contact.email} entrou em contato pelo site',
        sender=app.config.get("MAIL_USERNAME"),
        recipients=["viniciosdb@gmai.com", app.config.get("MAIL_USERNAME")],
        body=f'''
            Nome: {new_contact.name}
            Email: {new_contact.email}
            Telefone: {new_contact.phone}
            Mensagem: {new_contact.message}
        '''
    )

    mail.send(message)


def clear_form(form):
    form.name.data = ""
    form.email.data = ""
    form.phone.data = ""
    form.message.data = ""

