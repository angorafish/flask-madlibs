from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_questions():
    """Create and display form to ask for madlib words."""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Show the story based on the form filled out."""
    text = story.generate(request.args)
    return render_template("story.html", text=text)
