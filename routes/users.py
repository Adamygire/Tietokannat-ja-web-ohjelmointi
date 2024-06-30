from flask import flash, render_template, request, redirect

from app import app
import users


@app.route("/signup", methods=["get", "post"])
def signup():
    if request.method == "POST":
        print("[POST] /signup - FORM:", request.form)

        name = request.form["name"]
        if len(name) < 3 or len(name) > 20:
            return render_template(
                "error.html", message="Tunnuksessa tulee olla 3-20 merkkiä"
            )

        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        if not users.signup(name, email, password, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

        flash("You have created the course.")
        return redirect("/")

    return render_template("users/signup.html")


@app.route("/signin", methods=["get", "post"])
def signin():
    if request.method == "POST":
        print("[POST] /signin - FORM:", request.form)
        email = request.form["email"]
        password = request.form["password"]

        if not users.signin(email, password):
            return render_template("error.html", message="Incorrect email or password")
        return redirect("/")
    return render_template("users/signin.html")


@app.route("/signout")
def signout():
    users.signout()
    return redirect("/")
