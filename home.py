from flask import Flask, request
from flask.templating import render_template
from stories import Story

app = Flask(__name__)

@app.route("/")
def home_page():
    """Shows home page."""
    return render_template("home.html")

