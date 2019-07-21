from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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


class Inventory(Base):
    """
    A declarative base for an inventory, which is mapped to
    the inventory table of the database.
    """

    __tablename__ = "inventory"

    userId = Column(ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    itemId = Column(Integer, primary_key=True)

    user = relationship("User")
