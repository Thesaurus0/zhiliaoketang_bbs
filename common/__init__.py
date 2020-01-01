from .views import  bp

def init_view_common(app):
    app.register_blueprint(bp)
