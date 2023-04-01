from flask_ngrok2 import run_with_ngrok

def __init__(self, app=None):
    if app is not None:
        self.init_app(app)

def init_app(self, app):
    app.before_request(
        ...)