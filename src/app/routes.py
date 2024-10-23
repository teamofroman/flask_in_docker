from modules.hello_world import hello_world_bp


def route(app):
    app.register_blueprint(hello_world_bp)
