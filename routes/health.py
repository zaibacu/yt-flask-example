from flask import make_response, Blueprint

bp = Blueprint('health', __name__)


@bp.route('/health')
def messages():
    return make_response('Ok')


@bp.route('/status')
def status():
    # if everything is OK - green
    # if some part is down - yellow
    # if everything is bad - red
    return make_response('green')
