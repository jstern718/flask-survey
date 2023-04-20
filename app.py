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

    title = survey.title
    instructions = survey.instructions

    return render_template("survey_start.html", title = title, instructions = instructions)

@app.post("/")
def load_question():

    # check our REPONSES list to see if empty
        # if its empty go to question 0
    # else
        # get last index add one to it to access next question

    # if RESPONSES

    return(redirect('/begin'))

@app.post("/begin")
def get_question_route():

    return redirect("/questions/0")

@app.get("/questions/0")
def get_question_route2():

    question = survey.questions[0].prompt
    choices = survey.questions[0].choices

    return render_template("question.html", question = question, choices = choices)






