from app import app
from flask import render_template, request, redirect, url_for
from .form import MyLoginForm
from functools import wraps

session = []

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('home.html',
                           titolo='Home')

@app.route('/login', methods=('GET', 'POST'))
def login(error = None):
    form = MyLoginForm(request.form)
    if form.validate_on_submit():
        if form.username.data == 'Demo':
            if form.password.data == 'Password':
                session.append('logged_in')
                return redirect(url_for("index"))
            else:
                error = "Username o Password, errati!"
        else:
            error = "Username o Password, errati!"
    elif form.username.data == '' or form.password.data == '':
        error = "Username o Password, errati!"
    return render_template('login.html',
                           titolo='Accedi',
                           form = form,
                           error = error)

@app.route('/esci')
@login_required
def log_out():
    session.remove('logged_in')
    return redirect(url_for('login'))