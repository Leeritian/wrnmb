from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello u'


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        body = request.form['body']
        if body is None:
            body = 'shabi'
        return render_template('test.html', body=body)
    return render_template('test.html')


if __name__ == '__main__':
    app.run()

