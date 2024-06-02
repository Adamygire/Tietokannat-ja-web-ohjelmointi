import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def signup(name, email, password):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (name, email, password)
                 VALUES (:name, :email, :password)"""
        db.session.execute(text(sql), {"name":name, "email":email, "password":hash_value})
        db.session.commit()
    except Exception as error:
        print(error)
        return False
    return signin(email, password)

def signin(email, password):
    sql = "SELECT password, id, role FROM users WHERE email=:email"
    result = db.session.execute(text(sql), {"email":email})
    user = result.fetchone()
    print("user: ", user)
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    session["user_id"] = user[1]
    session["user_email"] = email
    session["user_role"] = user[2]
    session["csrf_token"] = os.urandom(16).hex()
    return True

def signout():
    del session["user_id"]
    del session["user_email"]

def user_id():
    return session.get("user_id", 0)

def user_role():
    return session.get("user_role", 0)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

