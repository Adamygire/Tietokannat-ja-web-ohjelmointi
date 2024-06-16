from os import getenv
from flask_sqlalchemy import SQLAlchemy
from app import app

if getenv("DATABASE_URL").startswith("postgre"):
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace(
        "://", "ql://", 1
    )
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

db = SQLAlchemy(app)
