from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/")
def home_page():
    """Shows home page."""

    return render_template("home.html", prompts=story.prompts)

@app.route("/story")
def story_page():
    """Shows story page."""
    return render_template("story.html", text=story.generate(request.args))
