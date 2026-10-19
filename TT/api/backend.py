from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from sqlalchemy import Integer, Column, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

import os

DATABASE_URL = os.environ.get(
    "DATABASE_URL", 
    "postgresql://postgres:0208_password@127.0.0.1:8120/demo"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

class cc_users(Base):
    __tablename__ = "users"
    id = Column(Integer, nullable=False, primary_key=True)


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/p")
async def create_user(data: Item, db: Session = Depends(get_db)):
    new_user = cc_users(id=data.id)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"status": "success", "message": f"Successfully saved user: {new_user.id}"}
    except Exception as error:
        db.rollback()
        return {"status": "error", "message": "failed to save user", "error": str(error)}

@app.delete("/d")
async def del_user(data: Item, db: Session = Depends(get_db)):
    find_user = db.query(cc_users).filter(cc_users.id == data.id).first()
    if not find_user:
        return {"status": "error", "message": "User not found"}
    try:
        db.delete(find_user)
        db.commit()
        return {"status": "success", "message": f"Successfully deleted user: {data.id}"}
    except Exception as error:
        db.rollback()
        return {"status": "error", "message": "failed to delete user", "error": str(error)}
