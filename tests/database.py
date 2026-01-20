# import pytest
# from fastapi.testclient import TestClient
# from app.main import app
# from app.config import settings
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.database import get_db, Base


# SQL_ALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

# engine = create_engine(SQL_ALCHEMY_DATABASE_URL, echo=True)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# @pytest.fixture
# def session():
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#     Base.metadata.drop_all(bind=engine)
    
# @pytest.fixture
# def client(session):
#     def override_get_db():
#         yield session
#     app.dependency_overrides[get_db] = override_get_db
#     yield TestClient(app)