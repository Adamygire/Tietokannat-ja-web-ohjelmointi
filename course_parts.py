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
