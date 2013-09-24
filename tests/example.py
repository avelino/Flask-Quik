from flask import Flask
from flask.ext.quik import FlaskQuik
from flask.ext.quik import render_template


app = Flask(__name__)
quik = FlaskQuik(app)


@app.route('/', methods=['GET', 'POST'] )
def hello_quik():
    return render_template('hello.html', name='quik')


app.run(host='0.0.0.0', debug=True, port=5000)
