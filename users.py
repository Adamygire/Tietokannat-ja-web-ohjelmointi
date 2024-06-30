from datetime import datetime
import os
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from db import db


def signup(name, email, password, role):
    args = {
        "name": name,
        "email": email,
        "role": role,
        "password": generate_password_hash(password),
        "created_at": datetime.now(),
    }
    print("users.signup - args:", args)

    try:
        sql = """INSERT INTO users (name, email, password, role, created_at)
                 VALUES (:name, :email, :password, :role, :created_at)"""
        db.session.execute(text(sql), args)
        db.session.commit()
    except Exception as error:
        print("users.signup - error:", error)
        return False
    return signin(email, password)


def signin(email, password):
    result = db.session.execute(
        text("SELECT id, password, role, name FROM users WHERE email=:email"),
        {"email": email},
    )
    user_tuple = result.fetchone()
    if not user_tuple:
        return False

    userid, pwhash, userrole, user_name = user_tuple
    if not check_password_hash(pwhash, password):
        return False

    session["user_id"] = userid
    session["user_name"] = user_name
    session["user_email"] = email
    session["user_role"] = userrole
    session["csrf_token"] = os.urandom(16).hex()
    return True


def signout():
    del session["user_id"]
    del session["user_name"]
    del session["user_email"]
    del session["user_role"]
    del session["csrf_token"]


def user_id():
    return session.get("user_id", 0)


def user_role():
    return session.get("user_role", 0)


def check_csrf():
    if session.get("csrf_token", 0) != request.form["csrf_token"]:
        print("[ERROR]: CSFR")
        abort(403)
