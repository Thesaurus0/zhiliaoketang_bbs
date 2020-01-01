from .views import  bp

def init_view_cms(app):
    app.register_blueprint(bp)
