from flask import render_template, Blueprint, request

from models import Contact
from database import db

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        print('Got some data! {}'.format(data))
        first_name = data['first_name']
        last_name = data['last_name']
        c = Contact(
            first_name=first_name,
            last_name=last_name,
            email=data['email'],
            text=data['text']
        )
        db.session.add(c)
        db.session.commit()

        return render_template('thank-you.html',
                               name='{first_name} {last_name}'.format(
                                   first_name=first_name,
                                   last_name=last_name
                               ))
    else:
        return render_template('contact.html')
