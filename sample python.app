from flask import Flask

import os

app = Flask(__name__)

@app.route("/")
def db():
    return "welcome to dbots!!!"

app.run(host="0.0.0.0", port=8080)    
