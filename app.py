# backend -> frontend, frontend -> backend (jinja from Flask)
# from crypt import methods
from flask import Flask, render_template, url_for
import requests
from flask import request as req


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")


@app.route("/Summarise", methods=["GET", "POST"])
def Summarise():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        data = req.form["data"]

        minL = 20
        maxL = 70

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query(
            {
                "inputs": data,
                "parameters": {
                    "min_length": minL,
                    "max_length": maxL,
                },
            }
        )
        return render_template("index.html", result=output)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
