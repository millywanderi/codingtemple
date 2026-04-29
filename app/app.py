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

# app factory
def create_app(config_name=None):
    app = Flask(__name__)

    # Config
    if config_name == "TestingConfig":
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)

    # routes
    @app.route('/members/', methods=['POST'])
    def create_member():
        data = request.get_json()

        errors = {}

        # validation
        if 'email' not in data:
            errors['email'] = ['Missing data for the required field.']
        if 'name' not in data:
            errors['name'] = ['Missing data for required field.']
        if 'DOB' not in data:
            errors['DOB'] = ['Missing data for required field.']
        if 'password' not in data:
            errors['password'] = ['Missing data for required field.']

        if errors:
            return jsonify(errors), 400

        try:
            dob = datetime.strptime(data['DOB'], "%Y-%m-%d").date()
        except Exception:
            return jsonify({"DOB": ["Invalid date format."]}), 400

        member = Member(
            name=data['name'],
            email=data['email'],
            DOB=dob,
            password=data['password']
        )
        db.session.add(member)
        db.session.commit()

        return jsonify({
            "id": member.id,
            "name": member.name,
            "email": member.email
        }), 201

    # login
    @app.route('/members/login', methods=['POST'])
    def login_member():
        data = request.get_json()

        member = Member.query.filter_by(email=data.get('email')).first()

        if not member or member.password != data.get('password'):
            return jsonify({
                "message": "Invalid email or password!"
            }), 400

        token = encode_token(member.id, 'admin')

        return jsonify({
            "status": "success",
            "token": token
        }), 200

    # Update Member (Protected)
    @app.route('/members/', methods=['PUT'])
    def update_member():
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({"message": "Token Missing!"}), 401

        token = auth_header.split(" ")[1]
        decoded = decode_token(token)

        if not decoded:
            return jsonify({"message": "Invalid Token"}), 401

        member = Member.query.get(decoded['user_id'])
        if not member:
            return jsonify({"message": "User not found"}), 404

        data = request.get_json()

        # Only update if value provided
        if data.get('name'):
            member.name = data['name']

        if data.get('email'):
            member.email = data['email']

        if data.get('password'):
            member.password = data['password']

        db.session.commit()

        return jsonify({
            "id": member.id,
            "name": member.name,
            "email": member.email
        }), 200

    return app
