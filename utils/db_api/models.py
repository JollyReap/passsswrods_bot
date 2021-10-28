from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    VARCHAR
)
from sqlalchemy.ext.declarative import declarative_base  # класс, от которого будем наследовать все таблицы БД
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    tg_id = Column(Integer, nullable=False, unique=True)
    password_id = Column(Integer, ForeignKey('password.id'), nullable=True, unique=True)
    ship = relationship("user", backref="users")


class Password(Base):
    __tablename__ = "password"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    service = Column(String(20), nullable=False, unique=False)
    email = Column(String(50), nullable=False, unique=False)
    password = Column(VARCHAR(100), nullable=False, unique=False)
    relation = relationship('passwords', backref="password")

