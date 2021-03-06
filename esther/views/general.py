from flask import (Blueprint, current_app, request, flash, render_template,
                   redirect, url_for)

from esther import mail
from esther.models import Post
from esther.forms import ContactForm

blueprint = Blueprint('general', __name__)

@blueprint.route('/', defaults={'page': 1})
@blueprint.route('/page/<int:page>')
def index(page):
    recent_posts = Post.get_recent(page)
    return render_template('general/index.html', posts=recent_posts)

@blueprint.route('/about')
def about():
    return render_template('general/about.html')

@blueprint.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        email_body = render_template('general/email.txt', form=form)

        mail.send_message(
            sender=current_app.config['CONTACT_EMAIL_SENDER'],
            recipients=current_app.config['CONTACT_EMAIL_RECIPIENTS'],
            subject=current_app.config['CONTACT_EMAIL_SUBJECT'],
            body=email_body
        )

        flash(u'Your message has been sent. I will get back to you as soon '
              'as possible.', 'success')
        return redirect(url_for('.index'))

    return render_template('general/contact.html', form=form)
