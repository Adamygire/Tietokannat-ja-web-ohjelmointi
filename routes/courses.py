from flask import flash, render_template, request, redirect

from app import app
from constants import Role
import users
import courses
import course_parts


@app.route("/courses", methods=["get", "post"])
def courses_index():
    if request.method == "POST":
        print("[POST] /courses - FORM:", request.form)
        users.check_csrf()

        name = request.form["name"]
        subject = request.form["subject"]
        starts = request.form["starts"]
        ends = request.form["ends"]

        if users.user_role() != Role.TEACHER.value:
            return render_template("error.html", message="You are not a teacher!")

        if ends < starts:
            return render_template(
                "error.html", message="A course can not end before it starts!"
            )

        if not courses.new(name, subject, starts, ends, users.user_id()):
            return render_template("error.html", message="Luonti ei onnistunut")
        return redirect("/courses")

    course_list = courses.get_all()
    return render_template(
        "courses/list.html", courses=course_list, count=len(course_list)
    )


@app.route("/courses/new")
def courses_new():
    return render_template("courses/new.html")


@app.route("/courses/<int:course_id>")
def course_view(course_id):
    course = courses.get(course_id)
    is_enrolled = courses.is_enrolled(course_id)
    students = courses.get_students(course_id)
    print(f"course_view: is_enrolled={is_enrolled}")
    return render_template(
        "courses/view.html",
        course=course,
        is_enrolled=is_enrolled,
        parts=course_parts.get_all(course_id),
        students=students,
    )


@app.route("/courses/<int:course_id>/edit", methods=["get", "post"])
def course_edit(course_id):
    if request.method == "POST":
        print(f"[POST] /courses/{course_id}/edit - FORM:", request.form)
        users.check_csrf()
    else:
        print(f"[GET] /courses/{course_id}/edit")
    return render_template("error.html", message="Not implemented.")


@app.route("/courses/<int:course_id>/delete", methods=["post"])
def course_delete(course_id):
    print(f"[POST] /courses/{course_id}/delete - FORM:", request.form)

    course = courses.get(course_id)
    if course[-1] == users.user_id():
        flash(f"You have deleted the course: {course[1]}.")
        courses.delete(course_id)
        return redirect("/courses")
    return render_template("error.html", message="You did not create this course.")


@app.route("/courses/<int:course_id>/enroll", methods=["post"])
def course_enroll(course_id):
    print(f"[POST] /courses/{course_id} - FORM:", request.form)
    user_id = request.form["user_id"]
    if courses.enroll(course_id, user_id):
        flash("You have enrolled to this course.")
        return redirect(f"/courses/{course_id}")
    return render_template(
        "error.html", message="There was an error while enrolling to course."
    )


@app.route("/courses/<int:course_id>/unenroll", methods=["post"])
def course_unenroll(course_id):
    print(f"[POST] /courses/{course_id}/unenroll - FORM:", request.form)
    user_id = request.form["user_id"]
    if courses.unenroll(course_id, user_id):
        flash("You have unenrolled from this course.")
        return redirect(f"/courses/{course_id}")
    return render_template(
        "error.html", message="There was an error while unenrolling from this course."
    )
