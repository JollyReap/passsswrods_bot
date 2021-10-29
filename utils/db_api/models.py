from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    VARCHAR
)
from sqlalchemy.ext.declarative import declarative_base  # класс, от которого будем наследовать все таблицы БД
from sqlalchemy.orm import relationship
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"
    tg_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    # tg_id = Column(Integer, nullable=False, unique=True)
    password_id = Column(Integer, ForeignKey('Password.id'), nullable=True, unique=True)
    ship = relationship("Password", backref="Users")#primaryjoin='and_(Users.tg_id==Password.tg_user_id)')


class Password(Base):
    __tablename__ = "Password"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    tg_user_id = Column(Integer, ForeignKey("Users.tg_id"))
    service = Column(String(20), nullable=False, unique=False)
    email = Column(String(50), nullable=False, unique=False)
    password = Column(VARCHAR(100), nullable=False, unique=False)
    relation = relationship('Users', backref="Password", secondary='Users')

