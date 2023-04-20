from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []

#homepage route
@app.get("/")
def homepage():
    """Return homepage."""

    survey_title = survey.title
    print("print title:", survey_title)

    return render_template("survey_start.html")



