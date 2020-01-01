from .views import  bp

def init_view_front(app):
    app.register_blueprint(bp)
