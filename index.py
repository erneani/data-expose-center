from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/about")
def hello():
    return "Projeto para expor dados públicos minerados"