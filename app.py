# backend -> frontend, frontend -> backend (jinja from Flask)
from crypt import methods
from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def Index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()