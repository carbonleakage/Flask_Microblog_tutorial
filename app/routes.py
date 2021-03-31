from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sarav'}
    posts = [
        {
            'author':{'username': 'Brindha'},
            'body':'Beautiful day in Berlin!'
        },
        {
            'author':{'username': 'Sarav'},
            'body':'Raspberry Pi is here!'
        }
    ]
    return render_template('index.html', title = "Welcome", user = user, posts = posts)