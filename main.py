from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name : str

    class 

@app.post("/students/", status_code=200)
async def create_student(student: StudentCreateSchema):
    return student

@app.get

@app.get("/")
async def root():
    return {"message": "Hello World"}