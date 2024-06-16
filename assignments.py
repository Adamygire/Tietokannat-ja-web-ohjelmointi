from sqlalchemy.sql import text
from db import db


def new(part_id: int, assignment_type: int, question:str, answer: str, points: int):
    args = {
        "part_id": part_id,
        "type": assignment_type,
        "question": question,
        "answer": answer,
        "points": points,
    }

    print("assignments.new - args:", args)

    try:
        sql = """INSERT INTO Assignments (course_part_id, type, question, answer, points)
                 VALUES (:part_id, :type, :question, :answer, :points)"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("assignments.new - error:", error)
        return False
    return True


def get_all(part_id):
    args = {"id": part_id}
    sql = "SELECT id, course_part_id, type, question, answer, points FROM Assignments WHERE course_part_id = :id"
    print("assignments.new - args:", args)
    result = db.session.execute(text(sql), args)
    assignments = result.fetchall()
    print("assignments.get_all - assignments:", assignments)
    return assignments


def get(assignment_id):
    sql = "SELECT id, course_part_id, type, question, answer, points FROM Assignments WHERE id = :id"
    result = db.session.execute(text(sql), {"id": assignment_id})
    assignment = result.fetchone()
    return assignment


def delete(assignment_id):
    args = {"id": assignment_id}
    print("assignments.delete - args:", args)

    try:
        sql = """DELETE FROM Assignments WHERE id = :id"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("Assignments.delete - error:", error)
        return False
    return True
