from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/places")
def places():
    return render_template("places.html")

@app.route("/pic")
def pic():
    return render_template("pic.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
