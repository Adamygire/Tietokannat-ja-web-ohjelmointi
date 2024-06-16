from flask import flash, render_template, request, redirect

from app import app
import users
import courses
import course_parts
import assignments


@app.route("/parts/<int:part_id>/assignments", methods=["get", "post"])
def assignments_index(part_id):
    part = course_parts.get(part_id)

    if request.method == "POST":
        print(f"[POST] /parts/{part_id}/assignments - FORM:", request.form)

        if not assignments.new(
            part_id, request.form["type"], request.form["question"], request.form["answer"], request.form["points"]
        ):
            return render_template("error.html", message="Luonti ei onnistunut")
        return redirect(f"/parts/{part_id}")

    return render_template("assignments/new.html", part=part)


@app.route("/parts/<int:part_id>/assignments/<int:assignment_id>", methods=["get", "post"])
def assignment_view(part_id, assignment_id):
    part = course_parts.get(part_id)
    course_id = part[1]
    assignment = assignments.get(assignment_id)
    course = courses.get(course_id)

    if request.method == "POST":
        print(f"[POST] /parts/{course_id}/assignments - FORM:", request.form)
        return redirect("/courses")

    return render_template("assignments/view.html", course=course, assignment=assignment, part=part)



@app.route("/parts/<int:part_id>/assignments/<int:assignment_id>/edit", methods=["get", "post"])
def assignment_edit(part_id, assignment_id):
    part = course_parts.get(part_id)
    course_id = part[1]
    if request.method == "POST":
        print(f"[POST] /parts/{course_id}/assignments/{assignment_id}/edit - FORM:", request.form)
    else:
        print(f"[GET] /parts/{course_id}/assignments/{assignment_id}/edit")
    return render_template("error.html", message="Not implemented.")


@app.route("/parts/<int:part_id>/assignments/<int:assignment_id>/delete", methods=["post"])
def assignment_delete(part_id, assignment_id):
    part = course_parts.get(part_id)
    course_id = part[1]
    print(f"[POST] /parts/{course_id}/assignments/{assignment_id}/delete - FORM:", request.form)

    course = courses.get(course_id)
    if course[-1] == users.user_id():
        assignments.delete(assignment_id)
        flash(f"You have deleted the assignment: {assignment_id}.")
        return redirect(f"/parts/{course_id}")
    return render_template("error.html", message="You did not create this assignment!")

