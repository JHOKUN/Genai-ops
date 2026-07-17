from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort, redirect, url_for
from markupsafe import escape

app = Flask(__name__)
                                        #  http://127.0.0.1:5000/
@app.route('/')
def index():
    return 'Welcome to our home page.\n' \
            'Please find our other routes :\n' \
            '/hello\n' \
            '/user/<username>\n' \
            '/int_display/<int:int>'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Logged as {escape(username)}'

@app.route('/int_display/<int:int>')
def show_post(int):
    return f'Parameter : {int}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/redirect')
def redirect():
    return redirect(url_for('login'))

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@app.route('/login')
def login():
    abort(401)