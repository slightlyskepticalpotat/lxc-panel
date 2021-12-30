from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Pretend this is a LXC frontend."
