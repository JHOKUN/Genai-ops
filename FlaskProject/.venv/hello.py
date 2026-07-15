from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to our home page.\n' \
            'Please find our other routes :\n' \
            '/hello\n' \
            '/user/<username>\n' \
            '/int_display/<int:int>'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Logged as {escape(username)}'

@app.route('/int_display/<int:int>')
def show_post(int):
    return f'Parameter : {int}'