from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.0.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
