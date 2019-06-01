import json

from flask import render_template, Blueprint

bp = Blueprint('admin', __name__)


@bp.route('/messages')
def messages():
    with open('data/contact.jsonl', 'r') as f:
        raw = f.readlines()

    msgs = [json.loads(line) for line in raw]

    return render_template('messages.html', messages=msgs)
