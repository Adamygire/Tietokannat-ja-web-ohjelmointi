from flask import render_template
from . import courses, course_parts, users, assignments


from app import app

@app.route("/")
def index():
    return render_template("index.html")

