from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('test'))


@app.route('/test')
def test():
    return redirect(url_for('receive', requestform=''))

