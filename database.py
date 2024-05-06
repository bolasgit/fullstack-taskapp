from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://taskapp_wq5l_user:KafmTz4cjeyg8oaZ0OIjx0dyQBn5cZG2@dpg-cortici0si5c739mbigg-a.oregon-postgres.render.com/taskapp_wq5l"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
