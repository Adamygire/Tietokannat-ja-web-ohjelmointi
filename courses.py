from datetime import datetime

from flask import session
from sqlalchemy.sql import text

from db import db


def new(name, subject, starts, ends, teacher_id):
    args = {
        "name": name,
        "subject": subject,
        "starts": starts,
        "ends": ends,
        "teacher_id": teacher_id,
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


def get_all():
    sql = "SELECT id, name, subject, starts, ends FROM Courses"
    result = db.session.execute(text(sql))
    courses = result.fetchall()
    return courses


def get(course_id):
    sql = (
        "SELECT id, name, subject, starts, ends, teacher_id FROM Courses WHERE id = :id"
    )
    result = db.session.execute(text(sql), {"id": course_id})
    course = result.fetchone()
    return course


def enroll(course_id, user_id):
    args = {"course_id": course_id, "user_id": user_id, "enrolled": datetime.now()}

    print("courses.enroll - args:", args)

    try:
        sql = """INSERT INTO Enrolments (course_id, student_id, enrolled)
                 VALUES (:course_id, :user_id, :enrolled)"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("courses.enroll - error:", error)
        return False
    return True


def unenroll(course_id, user_id):
    args = {"course_id": course_id, "user_id": user_id}
    print("courses.unenroll - args:", args)

    try:
        sql = """DELETE FROM Enrolments WHERE course_id = :course_id and student_id = :user_id"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("courses.unenroll - error:", error)
        return False
    return True


def is_enrolled(course_id):
    sql = "SELECT * FROM Enrolments WHERE course_id = :course_id and student_id = :student_id"
    result = db.session.execute(
        text(sql), {"course_id": course_id, "student_id": session["user_id"]}
    )
    enrollment = result.fetchone()
    print(f"enrollment: {enrollment}")
    return enrollment is not None


def edit(course_id, name, subject, starts, ends):
    args = {
        "course_id": course_id,
        "name": name,
        "subject": subject,
        "starts": starts,
        "ends": ends,
    }

    print("courses.edit - args:", args)

    try:
        sql = """UPDATE Courses
                SET
                    name = :name,
                    subject = :subject,
                    starts = :starts,
                    ends = :ends
                WHERE id = :course_id"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("courses.edit - error:", error)
        return False
    return True


def delete(course_id):
    args = {"course_id": course_id}
    print("courses.delete - args:", args)

    try:
        sql = """DELETE FROM Courses WHERE id = :course_id"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("courses.delete - error:", error)
        return False
    return True


def stats(course_id):
    pass
