from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from sqlalchemy import Integer, Column, VARCHAR, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

class Item(BaseModel):
    id: int

@app.post("/p")
async def receive_data(data: Item):
    received_id = data.id

    return {"status": "success", "message": f"saved info: {received_id}"}
