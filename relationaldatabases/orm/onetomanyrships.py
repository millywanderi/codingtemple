#!/usr/bin/env python3

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship
from typing import List, Optional

# A user can have multiple pets but each pet has only 1 owner
engine = create_engine('mysql+mysqlconnector://millie:ciku2015@localhost/intro_orm', echo=True)

# Base class for models
class Base(DeclarativeBase):
    pass


# User model
class User(Base):
    __tablename__ = "user_account"

    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(200))
    
    # One-to-Many: User -> List of Pet objects
    pets: Mapped[List["Pet"]] = relationship(back_populates="owner", cascade="all, delete-orphan")


# Pet model
class Pets(Base):
    __tablename__ = "pets"

    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    animal: Mapped[str] = mapped_column(String(200))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    # Many-to-One: Pet -> User
    owner: Mapped["User"] = relationship(back_populates="pets")

# create tables
Base.metadata.create_all(engine)

session = Session(engine)

new_user = User(name="Peter", fullname="Peter John")
session.add(new_user)
session.commit()
