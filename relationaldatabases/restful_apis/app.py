#!/usr/bin/env python3

# Configure the Flask app and connect it to MySQL
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, Table, Column, String, Integer
from marshmallow import ValidatorError
from typing import List, Optional
#from __future__ import annotations
import os

# Initialize Flask app
app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://millie:ciku2015@localhost/flask_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating our Base Model
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)

# Association Table
user_pet = Table(
        "user_pet",
        Base.metadata,
        Column("user_id", ForeignKey("user_account.id"), primary_key=True),
        Column("pet_id", ForeignKey("pets.id"), primary_key=True)
)

# Models
class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(200))

    #One-to-Many relationship from this User to a List of Pet Objects
    pets: Mapped[List["Pet"]] = relationship("Pet", secondary=user_pet, back_populates="owners")


class Pet(Base):
    __tablename__ = "pets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    animal: Mapped[str] = mapped_column(String(200), nullable=False)

    # One-to-Many relationship, One pet can be related to a List of Users
    owners: Mapped[List["User"]] = relationship("User", secondary=user_pet, back_populates="pets")

#User Schema
class UserSchema(Ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Pet Schema
class PetSchema(Ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pet

# Initialize Schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)

# Creating API Endpoints (User)
@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.message), 400

    new_user = User(name=user_data['name'], email=user_data['email'])
    db.session.add()
    db.session.commit()

    return user_schema.jsonify(new_user), 201

# Read All Users
@app.users('/users', methods=['GET'])
def get_users():
    query = select(User)
    users = db.session.execute(query).scalars().all()

    return users_schema.jsonify(users), 200

# Read a Single User by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = db.session.get(User, id)
    return user_schema.jsonify(user), 200


if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()

    app.run(debug=True)
