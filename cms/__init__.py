from .views import  bp
from .models import CMSUser

def init_view_cms(app):
    app.register_blueprint(bp)
