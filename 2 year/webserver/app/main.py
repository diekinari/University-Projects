from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from databases import Database

# from app.models import Base, User  # Import your models

# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/mydatabase"
#
# database = Database(DATABASE_URL)
# metadata = MetaData()
#
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup():
    # Connect to the database
    # await database.connect()
    pass


@app.on_event("shutdown")
async def shutdown():
    # Disconnect from the database
    # await database.disconnect()
    return {"Shutdown": "True"}

# Example endpoint to get users
# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     async with database.transaction():
#         query = User.select().where(User.c.id == user_id)
#         user = await database.fetch_one(query)
#         return user
