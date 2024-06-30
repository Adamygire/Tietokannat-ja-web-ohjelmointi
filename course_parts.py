from sqlalchemy.sql import text
from db import db


def new(course_id, material, deadline):
    args = {"course_id": course_id, "material": material, "deadline": deadline}

    print("course_parts.new - args:", args)

    try:
        sql = """INSERT INTO CourseParts (course_id, material, deadline)
                 VALUES (:course_id, :material, :deadline)"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("course_parts.new - error:", error)
        return False
    return True


def get_all(course_id):
    sql = "SELECT id, course_id, material, deadline FROM CourseParts WHERE course_id = :id"
    result = db.session.execute(text(sql), {"id": course_id})
    parts = result.fetchall()
    print(f"all parts = {parts}")
    return parts


def get(part_id):
    sql = "SELECT id, course_id, material, deadline FROM CourseParts WHERE id = :id"
    result = db.session.execute(text(sql), {"id": part_id})
    part = result.fetchone()
    return part


def delete(part_id):
    args = {"part_id": part_id}
    print("course_parts.delete - args:", args)

    try:
        sql = """DELETE FROM CourseParts WHERE id = :part_id"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("course_parts.delete - error:", error)
        return False
    return True


def get_score(part_id, student_id):
    args = { "part_id": part_id, "student_id":student_id }
    sql = "SELECT sum(score), sum(points) FROM Scores JOIN Assignments ON Assignments.id = assignment_id WHERE course_part_id = :part_id and student_id = :student_id"
    print("assignments.get_score - args:", args)
    result = db.session.execute(text(sql), args)
    score = result.fetchone()
    print("assignments.get_score - assignments:", score)
    return score


def get_stats(part_id):
    args = { "part_id": part_id }
    sql = "SELECT name, email, sum(score), sum(points)  FROM Scores JOIN Assignments, Users ON Assignments.id = assignment_id and Users.id = student_id WHERE course_part_id = :part_id"
    print("assignments.get_stats - args:", args)
    result = db.session.execute(text(sql), args)
    answer = result.fetchall()
    print("assignments.get_stats - assignments:", answer)
    return answer
