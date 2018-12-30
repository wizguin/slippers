from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    A declarative base for a user, which is mapped to
    the users table of the database.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    loginKey = Column(String)
    rank = Column(Integer)
    banned = Column(Integer)
    coins = Column(Integer)
    items = Column(String)
    buddies = Column(String)
    head = Column(Integer)
    face = Column(Integer)
    neck = Column(Integer)
    body = Column(Integer)
    hand = Column(Integer)
    feet = Column(Integer)
    color = Column(Integer)
    photo = Column(Integer)
    flag = Column(Integer)
