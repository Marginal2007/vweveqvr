from flask import Flask, render_template
from flask import request
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


@app.route('/austranaut_selection', methods=['GET', 'POST'])
def austranaut_method():
    if request.method == 'GET':
        return render_template('index4.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        return render_template('index4.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')