#!/usr/bin/env python3

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# create engine
engine = create_engine('mysql+mysqlconnector://millie:ciku2015@127.0.0.1:3306/intro_orm')

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)


Base.metadata.create_all(engine)
