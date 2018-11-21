from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def hello():
    return "Projeto para expor dados públicos minerados"

@app.route("/home")

@app.route("/home/<user>")
def home(user):
    return render_template('home.html',user=user)