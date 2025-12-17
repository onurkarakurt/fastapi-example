from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


# Conenct to your postgres DB with sqlachemy
#SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost/fastapi'
SQL_ALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Connect to your postgres DB with regular way
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='123456', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database conenction was succesfull!")
#         break
#     except Exception as error:
#         print("Conencting to database failed")
#         print("Error:", error)
#         time.sleep(5)