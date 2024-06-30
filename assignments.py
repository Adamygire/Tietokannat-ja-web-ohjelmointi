from datetime import datetime
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
    print("assignments.get_all - args:", args)
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


def new_answer(assignment_id, student_id, answer):
    args = {
        "assignment_id": assignment_id,
        "student_id": student_id,
        "answer": answer,
        "score": 5,
        "done": datetime.now()
    }

    print("assignments.answer - args:", args)

    try:
        sql = """INSERT INTO Scores (student_id, assignment_id, score, answer, done)
                 VALUES (:student_id, :assignment_id, :score, :answer, :done)"""

        print("excecute")
        db.session.execute(text(sql), args)
        print("commit")
        db.session.commit()
    except Exception as error:
        print("assignments.answer - error:", error)
        return False
    return True


def get_score(assignment_id, student_id):
    args = {
        "assignment_id": assignment_id,
        "student_id": student_id
    }
    sql = "SELECT score, answer, done FROM Scores WHERE assignment_id = :assignment_id and student_id = :student_id ORDER BY score, done DESC LIMIT 1"
    print("assignments.get_answers - args:", args)
    result = db.session.execute(text(sql), args)
    answer = result.fetchone()
    print("assignments.get_answers - assignments:", answer)
    return answer


def get_stats(assignment_id):
    args = { "assignment_id": assignment_id }
    sql = "SELECT avg(score) FROM Scores WHERE assignment_id = :assignment_id"
    print("assignments.get_stats - args:", args)
    result = db.session.execute(text(sql), args)
    answer = result.fetchone()
    print("assignments.get_stats - assignments:", answer)
    return answer[0]
