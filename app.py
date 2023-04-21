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
def load_homepage():

    return(redirect('/begin'))

@app.post("/begin")
def start_survey():
    
    print("responses length before submitting answer ===>", len(RESPONSES))
    return redirect(f"/questions/{len(RESPONSES)}")

@app.get(f"/questions/<number>")
def get_question(number):

    question = survey.questions[len(RESPONSES)].prompt
    choices = survey.questions[len(RESPONSES)].choices

    return render_template("question.html", question = question, choices = choices)

@app.post("/answer")
def store_answer():

    answer = request.form["answer"]
    RESPONSES.append(answer)
    print("responses length after submitting answer ===>", len(RESPONSES))

    return redirect(f"/questions/{len(RESPONSES)}")











