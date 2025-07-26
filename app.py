from flask import Flask

app = Flask(__name__)

@app.route('/')
def homePage():
    return 'Hello'

@app.route('/dev')
def dev():
    return 'Hello dev'