from flask import Blueprint

bp = Blueprint('front', __name__)

@bp.route('/index/')
def index():
    return 'front home'

