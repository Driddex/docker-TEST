from fastapi import FastAPI, Depends
from pydantic import BaseModel

from sqlalchemy import Integer, Column, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DATA_BASE_URI = "postgresql://postgres:0208_password@127.0.0.1:8120/news_db"

engine = create_engine(DATA_BASE_URI)
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
base = declarative_base()

class create_user(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)

app_core = FastAPI(title='flask app')

class data_users(BaseModel):
    id: int

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app_core.post('/p')
async def post(data: data_users, db: Session = Depends(get_db)):
    db_data = create_user(id=data.id)
    
    try:
        db.add(db_data)
        db.commit()

        return {"status" : "succesfully"}
    except:
        return {"status": "failed"}

@app_core.delete('/d')
async def delete(user_id: int,data: data_users, db : Session = Depends(get_db)):
    user_record = db.query(create_user).filter(create_user.id==user_id).first()

    if not user_record:
        return {"status": "failed"}

    try:
        db.delete(user_record)
        db.commit()
        return {"status" : "succesfully"}
    except:
        return {"status" : "failed"}


@app_core.get('/g')
async def get(user_id: int, db: Session = Depends(get_db)):
    user_record = db.query(create_user).filter(create_user.id == user_id).first()
    
    if not user_record:
        return {"result": "not found"}

    return {"result": "found"}