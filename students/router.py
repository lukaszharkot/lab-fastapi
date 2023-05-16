from fastapi import APIRouter, HTTPException
from .schema import StudentUpdateSchema
from .storage import get_students

router = APIRouter()
students = get_students()

@router.post("/", status_code=200)
async def create_student(student: StudentUpdateSchema):
    student_id = len(students) + 1
    students[student_id] = student
    return {"student_id": student_id, "student": student}

@router.get("/{student_id}")
async def read_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student_id, "student": students[student_id]}
