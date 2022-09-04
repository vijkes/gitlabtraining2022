from flask import Flask

import os

app = Flask(__name__)

@app.route("/")
def db():
    return "<body bgcolor='teal'><h1>welcome to devbots vkk , <u>Khamba-gani</u>!!!</h1></body>"

app.run(host="0.0.0.0", port=8080)
