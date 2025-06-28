from databases import Database


DATABASE_URL = "postgresql://postgres:1234@localhost:5432/library-database"


database = Database(DATABASE_URL)


async def get_db() -> Database:
    return database