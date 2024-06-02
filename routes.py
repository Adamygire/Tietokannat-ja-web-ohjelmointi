from app import app
from flask import render_template, request, redirect
import users
import courses

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/signup", methods=["get", "post"])
def signup():
    if request.method == "GET":
        return render_template("users/signup.html")

    if request.method == "POST":
        print("form", request.form)
        name = request.form["name"]
        if len(name) < 3 or len(name) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 3-20 merkkiä")

        email = request.form["email"]
        password = request.form["password"]

        if not users.signup(name, email, password):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        return redirect("/")



@app.route("/signin", methods=["get", "post"])
def signin():
    if request.method == "GET":
        return render_template("users/signin.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if not users.signin(email, password):
            return render_template("error.html", message="Incorrect email or password")
        return redirect("/")


@app.route("/signout")
def signout():
    users.signout()
    return redirect("/")



@app.route("/courses")
def list_courses():
    course_list = courses.list()
    return render_template("courses/list.html", courses=course_list, count=len(course_list))


@app.route("/courses/<int:course_id>")
def view_course(course_id):
    course= courses.view(course_id)
    return render_template("courses/view.html", course=course)



@app.route("/courses/new", methods=["get", "post"])
def new_course():
    if request.method == "GET":
        return render_template("courses/new.html")

    if request.method == "POST":
        print("[POST] /courses/new - FORM:", request.form)

        name = request.form["name"]
        subject = request.form["subject"]
        starts = request.form["starts"]
        ends = request.form["ends"]

        if users.user_role() != 2:
            return render_template("error.html", message="You are not a teacher!")

        if ends < starts:
            return render_template("error.html", message="A course can not end before it starts!")

        if not courses.new(name, subject, starts, ends, users.user_id()):
            return render_template("error.html", message="Luonti ei onnistunut")
        return redirect("/")
