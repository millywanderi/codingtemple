#!/usr/bin/env python3

from sqlalchemy import create_engine, String, Table, Column, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship
from typing import List, Optional

# Database connection
engine = create_engine('mysql+mysqlconnector://millie:ciku2015@localhost/relationships', echo=True)

# Base class for models
class Base(DeclarativeBase):
    pass


# Association table for User and Pet
user_pet = Table(
        "user_pet",
        Base.metadata,
        Column("user_id", ForeignKey("user_account.id")),
        Column("pet_id", ForeignKey("pets.id")),
)

# User model
class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(100))

    # Many-to-Many: User <-> Pet
    pets: Mapped[List["Pet"]] = relationship(secondary=user_pet, back_populates="owners")


# Pet model
class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    animal: Mapped[str] = mapped_column(String(100))

    # Many-to-Many: Pet <-> User
    owners: Mapped[List["User"]] = relationship(secondary=user_pet, back_populates="pets")

# Create Tables
Base.metadata.create_all(engine)

# Creating User and Pet Objects
session = Session(engine)

mother = User(name="Alice", email="awonderland@email.com")
son = User(name="Peter", email="pcottontail@email.com")

dog = Pet(name="Buddy", animal="dog")
goldfish = Pet(name="Goldy", animal="fish")

# Add all new objects into session
session.add(mother)
session.add(son)
session.add(dog)
session.add(goldfish)
session.commit()
