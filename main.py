from flask import Flask, render_template
from flask import request
app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('page.html', title=title)


@app.route('/index/<title>')
def index1(title):
    return render_template('page.html', title=title)


@app.route('/training/<prof>')
def index2(prof):
    return render_template('page.html', prof=prof)


@app.route('/image_mars')
def mars():
    return render_template('index1.html')


@app.route('/promotion_image')
def promotion():
    return render_template('index2.html')


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_method():
    if request.method == 'GET':
        return render_template('index4.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['gender'])
        print(request.form['motivation'])
        print(request.form['stay_on_mars'])
        return render_template('index4.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')