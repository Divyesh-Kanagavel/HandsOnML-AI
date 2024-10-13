# simple web application before embedding movie classifier into a web server
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('first_app.html')

if __name__ == '__main__':
    app.debug = True
    app.run()