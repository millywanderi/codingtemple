#!/usr/bin/env python3

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, 
mapped_column, relationship
from typing import List, Optional

# A user can have multiple pets but each pet has only 1 owner
engine = create_engine('mysql+mysqlconnector://root:ciku2015@localhost/mypetdatabase', echo=True)

# Base class for models
class Base(DeclarativeBase):
    pass


# User model
class User(Base):
    __tablename__ = "user_account"

    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: MappedOptional[[str]] = mapped_column(String(200))
    
    # One-to-Many: User -> List of Pet objects
    pets: Mapped[List["Pet"]] = relationship(back_populates="owner", cascade="all, delete_orphan")

