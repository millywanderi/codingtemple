#!/usr/bin/env python3

# The Base class serves as a foundation for all database models.
class Base(DeclaritiveBase):
    pass


# The User Class (A Model Representing a Table)
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(100))
