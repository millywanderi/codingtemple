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
        Column("pet_id", ForeignKey(pets.id)),
)
