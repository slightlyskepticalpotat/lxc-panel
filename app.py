import os

from flask import Flask, redirect, request, session, url_for
from flask_session import Session

from utils import login_required

app = Flask(__name__)

app.config.from_object("settings")
Session(app)

@app.route("/")
def index():
    if not session or "username" not in session:
        return redirect(url_for('login', next=request.url))
    return "Pretend this is a LXC frontend."

@app.route("/login")
def login():
    session.clear()
    return "Pretend this is a login page."
