from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name : str

    class StudentUpdateSchema:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

@app.post("/students/", status_code=200)
async def create_student(student: StudentCreateSchema):
    return student

@app.get("/students/{student_id}")
async def read_student(student_id):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student": students[student_id]}

@app.get("/")
async def root():
    return {"message": "Hello World"}
