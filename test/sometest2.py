from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test2.html')


@app.route('/test')
def test():
    return "yeah success"


if __name__ == '__main__':
    app.run()

