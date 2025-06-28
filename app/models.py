from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    publication_year = Column(Integer)
    isbn = Column(String, unique=True, index=True)
    image_url = Column(String, nullable=True)  # URL изображения
    available = Column(Boolean, default=True)
    description = Column(String, nullable=True)

class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    issue_date = Column(Date)
    return_date = Column(Date, nullable=True)