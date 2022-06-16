from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/add/<num1>/<num2>")
def add(num1, num2):    
    return render_template('add.html', n1=int(num1), n2=int(num2))