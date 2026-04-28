#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import jwt

db = SQLAlchemy()
SECRETE_KEY = "secret"

# Model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Token Helpers
def encode_token(user_id, role):
    payload = {
        "user_id": user_id,
        "role": role
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token):
    try:
        return jwt.encode(payload, SECRET_KEY, algorithms=["HS256"])
    except Exception:
        return None
