from flask import Blueprint

plans_bp = Blueprint('users', __name__, url_prefix='/users/')


@plans_bp.get('/helo/')
def helo():
    return 'hello!'
