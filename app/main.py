from fastapi import FastAPI, Depends, HTTPException
from databases import Database
from .database import database, get_db
from .schemas import UserCreate, UserResponse, BookCreate, BookResponse, LoanCreate, LoanResponse, UserLogin, UserUpdate
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Library API", description="API for managing a library system")


@app.on_event("startup")
async def startup():
    await database.connect()
    logger.info("Database connected successfully")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    logger.info("Database disconnected")

# Эндпоинт для создания пользователя
@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, db: Database = Depends(get_db)):
    query = """
        INSERT INTO users (username, password, email, phone)
        VALUES (:username, :password, :email, :phone)
        RETURNING id, username, email, phone
    """
    values = user.dict()
    logger.info(f"Attempting to create user with data: {values}")
    try:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            raise HTTPException(status_code=500, detail="Failed to create user: No result returned")
        logger.info(f"User created successfully: {dict(result)}")
        return dict(result)
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error creating user: {str(e)}")

# Эндпоинт для регистрации
@app.post("/register")
async def register(user: UserCreate, db: Database = Depends(get_db)):
    query = """
        INSERT INTO users (username, password, email, phone)
        VALUES (:username, :password, :email, :phone)
        RETURNING id, username, email, phone
    """
    values = user.dict()
    logger.info(f"Attempting to register user with data: {values}")
    try:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            raise HTTPException(status_code=500, detail="Failed to register user: No result returned")
        logger.info(f"User registered successfully: {dict(result)}")
        return {"access_token": f"fake_token_{result['id']}", "token_type": "bearer"}
    except Exception as e:
        logger.error(f"Error registering user: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error registering user: {str(e)}")

# Эндпоинт для логина
@app.post("/login")
async def login(user: UserLogin, db: Database = Depends(get_db)):
    query = """
        SELECT id, username, email, phone
        FROM users
        WHERE username = :username AND password = :password
    """
    values = user.dict()
    logger.info(f"Attempting to login user with username: {values['username']}")
    try:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        logger.info(f"User logged in successfully: {dict(result)}")
        return {"access_token": f"fake_token_{result['id']}", "token_type": "bearer"}
    except Exception as e:
        logger.error(f"Error logging in user: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error logging in user: {str(e)}")

# Эндпоинт для получения списка пользователей
@app.get("/users", response_model=list[UserResponse])
async def read_users(db: Database = Depends(get_db)):
    query = "SELECT id, username, email, phone FROM users"
    logger.info("Fetching all users")
    try:
        users = await db.fetch_all(query=query)
        logger.info(f"Fetched {len(users)} users")
        return users
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error fetching users: {str(e)}")

# Эндпоинт для создания книги
@app.post("/books", response_model=BookResponse)
async def create_book(book: BookCreate, db: Database = Depends(get_db)):
    query = """
        INSERT INTO books (title, author, publication_year, isbn, image_url, available, description)
        VALUES (:title, :author, :publication_year, :isbn, :image_url, :available, :description)
        RETURNING id, title, author, publication_year, isbn, image_url, available, description
    """
    values = book.dict()
    logger.info(f"Attempting to create book with data: {values}")
    try:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            raise HTTPException(status_code=500, detail="Failed to create book: No result returned")
        logger.info(f"Book created successfully: {dict(result)}")
        return dict(result)
    except Exception as e:
        logger.error(f"Error creating book: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error creating book: {str(e)}")

# Эндпоинт для получения списка книг
@app.get("/books", response_model=list[BookResponse])
async def read_books(db: Database = Depends(get_db)):
    query = "SELECT id, title, author, publication_year, isbn, image_url, available, description FROM books"
    logger.info("Fetching all books")
    try:
        books = await db.fetch_all(query=query)
        logger.info(f"Fetched books from DB: {books}")
        if not books:
            logger.warning("No books found in database")
            return []
        return books
    except Exception as e:
        logger.error(f"Error fetching books: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error fetching books: {str(e)}")

# Эндпоинт для выдачи книги
@app.post("/loans", response_model=LoanResponse)
async def create_loan(loan: LoanCreate, db: Database = Depends(get_db)):
    query = """
        INSERT INTO loans (book_id, user_id, issue_date, return_date)
        VALUES (:book_id, :user_id, :issue_date, :return_date)
        RETURNING id, book_id, user_id, issue_date, return_date
    """
    values = loan.dict()
    logger.info(f"Attempting to create loan with data: {values}")
    try:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            raise HTTPException(status_code=500, detail="Failed to create loan: No result returned")
        logger.info(f"Loan created successfully: {dict(result)}")
        return dict(result)
    except Exception as e:
        logger.error(f"Error creating loan: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error creating loan: {str(e)}")

# Эндпоинт для получения списка loans
@app.get("/loans", response_model=list[LoanResponse])
async def read_loans(db: Database = Depends(get_db)):
    query = "SELECT id, book_id, user_id, issue_date, return_date FROM loans"
    logger.info("Fetching all loans")
    try:
        loans = await db.fetch_all(query=query)
        logger.info(f"Fetched {len(loans)} loans")
        return loans
    except Exception as e:
        logger.error(f"Error fetching loans: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error fetching loans: {str(e)}")

# Эндпоинт для возврата книги
@app.delete("/loans/{loan_id}")
async def return_book(loan_id: int, db: Database = Depends(get_db)):
    query = "DELETE FROM loans WHERE id = :id RETURNING id"
    values = {"id": loan_id}
    logger.info(f"Attempting to return book with loan_id: {loan_id}")
    try:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            raise HTTPException(status_code=404, detail="Loan not found")
        logger.info(f"Book returned successfully for loan_id: {loan_id}")
        return {"message": "Book returned successfully"}
    except Exception as e:
        logger.error(f"Error returning book: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error returning book: {str(e)}")

# Эндпоинт для обновления пользователя
@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, db: Database = Depends(get_db)):
    query = """
        UPDATE users
        SET username = COALESCE(:username, username),
            password = COALESCE(:password, password),
            email = COALESCE(:email, email),
            phone = COALESCE(:phone, phone)
        WHERE id = :id
        RETURNING id, username, email, phone
    """
    values = user.dict(exclude_unset=True)
    values["id"] = user_id
    logger.info(f"Attempting to update user with id {user_id} with data: {values}")
    try:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"User updated successfully: {dict(result)}")
        return dict(result)
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error updating user: {str(e)}")