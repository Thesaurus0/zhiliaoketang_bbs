from flask import Blueprint

bp = Blueprint('cms', __name__,url_prefix='/cms')

@bp.route('/index/')
def index():
    return 'cms home'