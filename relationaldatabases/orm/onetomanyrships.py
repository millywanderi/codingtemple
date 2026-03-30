#!/usr/bin/env python3

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, 
mapped_column, relationship
from typing import List, Optional

# A user can have multiple pets but each pet has only 1 owner
engine = create_engine('mysql+mysqlconnector://root:ciku2015@localhost/mypetdatabase', echo=True)


