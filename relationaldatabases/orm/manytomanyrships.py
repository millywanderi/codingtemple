#!/usr/bin/env python3

from sqlalchemy import create_engine, String, Table, Column, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship
from typing import List, Optional

# Database connection
engine = create_engine('mysql+mysqlconnector://millie:ciku2015@localhost/relationships', echo=True)
