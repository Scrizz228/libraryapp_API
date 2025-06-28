from pydantic import BaseModel
from datetime import date
from typing import Optional

# Схема для логина
class UserLogin(BaseModel):
    username: str
    password: str

# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    phone: Optional[str] = None

# Схема для частичного обновления пользователя
class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

# Схема для ответа с данными пользователя
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    phone: Optional[str] = None

    class Config:
        orm_mode = True

# Схема для создания книги
class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int
    isbn: str
    image_url: Optional[str] = None  #  URL изображение
    available: Optional[bool] = True  # Доступность книги
    description: Optional[str] = None  # Описание книги

# Схема для ответа с данными книги
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    isbn: str
    image_url: Optional[str] = None  # URL изображениe
    available: Optional[bool] = True  # Доступность книги
    description: Optional[str] = None  # Описание книги

    class Config:
        orm_mode = True

# Схема для создания loan
class LoanCreate(BaseModel):
    book_id: int
    user_id: int
    issue_date: date
    return_date: Optional[date] = None

# Схема для ответа с данными loan
class LoanResponse(BaseModel):
    id: int
    book_id: int
    user_id: int
    issue_date: date
    return_date: Optional[date] = None

    class Config:
        orm_mode = True