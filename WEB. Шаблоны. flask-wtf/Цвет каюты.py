from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def table(sex: str, age: int):
    return render_template('design.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
