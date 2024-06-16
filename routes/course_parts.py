from flask import flash, render_template, request, redirect

from app import app
import users
import courses
import course_parts
import assignments


@app.route("/courses/<int:course_id>/parts", methods=["get", "post"])
def parts_index(course_id):
    course = courses.get(course_id)

    if request.method == "POST":
        print(f"[POST] /courses/{course_id}/parts - FORM:", request.form)

        if users.user_id() != course[-1]:
            return render_template(
                "error.html", message="You did not create this course!"
            )

        if not course_parts.new(
            course_id, request.form["material"], request.form["deadline"]
        ):
            return render_template("error.html", message="Luonti ei onnistunut")
        return redirect(f"/courses/{course_id}")

    return render_template("course_parts/new.html", course=course)


@app.route("/parts/<int:part_id>", methods=["get", "post"])
def part_view(part_id):
    part = course_parts.get(part_id)
    course_id = part[1]
    tasks = assignments.get_all(part_id)
    print(f"tasks={tasks}")
    course = courses.get(course_id)

    if request.method == "POST":
        print(f"[POST] /courses/{course_id}/parts - FORM:", request.form)
        return redirect("/courses")

    return render_template("course_parts/view.html", course=course, part=part, assignments=tasks)



@app.route("/parts/<int:part_id>/edit", methods=["get", "post"])
def part_edit(part_id):
    part = course_parts.get(part_id)
    course_id = part[1]
    if request.method == "POST":
        print(f"[POST] /courses/{course_id}/parts/{part_id}/edit - FORM:", request.form)
    else:
        print(f"[GET] /courses/{course_id}/parts/{part_id}/edit")
    return render_template("error.html", message="Not implemented.")


@app.route("/parts/<int:part_id>/delete", methods=["post"])
def part_delete(part_id):
    part = course_parts.get(part_id)
    course_id = part[1]
    print(f"[POST] /courses/{course_id}/parts/{part_id}/delete - FORM:", request.form)

    course = courses.get(course_id)
    if course[-1] == users.user_id():
        course_parts.delete(part_id)
        flash(f"You have deleted the part: {part_id}.")
        return redirect(f"/courses/{course_id}")
    return render_template("error.html", message="You did not create this part!")

