from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия колонизации Марса'


@app.route('/index')
def index1():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def index2():
    return render_template('index.html')


@app.route('/image_mars')
def mars():
    return render_template('index1.html')


@app.route('/promotion_image')
def promotion():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')