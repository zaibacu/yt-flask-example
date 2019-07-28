from flask import render_template, Blueprint
from models import Contact

bp = Blueprint('admin', __name__)


@bp.route('/messages')
def messages():
    results = Contact.query.all()
    return render_template('messages.html', messages=results)
