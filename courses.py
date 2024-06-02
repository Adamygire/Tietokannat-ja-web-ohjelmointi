from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def new(name, subject, starts, ends, teacher_id):
    args = {
            "name":name,
            "subject":subject,
            "starts":starts,
            "ends":ends,
            "teacher_id":teacher_id
    }

    print("courses.new - args:", args)

    try:
        sql = """INSERT INTO Courses (name, subject, starts, ends, teacher_id)
                 VALUES (:name, :subject, :starts, :ends, :teacher_id)"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("courses.new - error:", error)
        return False
    return True

def list():
    sql = "SELECT id, name, subject, starts, ends FROM Courses"
    result = db.session.execute(text(sql))
    courses = result.fetchall()
    print("courses: ", courses)
    return courses

def view(id):
    sql = "SELECT id, name, subject, starts, ends FROM Courses WHERE id == :id"
    result = db.session.execute(text(sql), {"id" :id})
    course = result.fetchone()
    print("course: ", course)
    return course
