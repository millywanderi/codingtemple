#!/usr/bin/env python3

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Member {self.email}>"
