#!/usr/bin/env python3

from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

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

# Insert data into the table
session = Session(engine)
email_to_insert = "john@example.com"
existing_user = session.execute(select(User).where(User.email == email_to_insert)).scalar_one_or_none()

if not existing_user:
    new_user = User(name="John", email="john@example.com")
    session.add(new_user)
    session.commit()
    print("User added:", existing_user.name, existing_user.email)
else:
    print("User already exists:", existing_user.name, existing_user.email)

# Query Data (SQL SELECT)
query = select(User)
users = session.execute(query).scalars().all()

for user in users:
    print(user.name, user.email)
