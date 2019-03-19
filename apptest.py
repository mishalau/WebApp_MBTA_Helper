from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import redirect, url_for, request
#import mbta_helper


@app.route('/')
def hello():
    return render_template('WebPageHello.html')

@app.route('/nearest/', methods =['POST', 'GET'])
def nearest():
    Location = request.form['Location']
    return render_template('Loading.html')

if __name__ == '__main__':
    app.run()
