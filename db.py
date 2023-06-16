from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mariadb+mariadbconnector://root:lol@127.0.0.1:3306/astrolabium")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Dependency
def get_db():
    db = SessionLocal()
    try:    
        yield db
    finally:
        db.close()                  
