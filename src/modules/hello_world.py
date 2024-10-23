from flask import Blueprint

hello_world_bp = Blueprint('hello_world', __name__)


@hello_world_bp.route('/')
def hello_world():
    return "<h1>Hello, World!<h1>"
