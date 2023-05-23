from fastapi import APIRouter, HTTPException
from .schema import StudentUpdateSchema, Mark
from .storage import get_students, get_marks

router = APIRouter()
students = get_students()
marks_storage = get_marks()

@router.post("/", status_code=200)
async def create_student(student: StudentUpdateSchema):
    student_id = len(students) + 1
    students[student_id] = student
    return {"student_id": student_id, "student": student}

@router.post("/{student_id}/marks/{ocena}")
async def add_mark(student_id: int, ocena: float):
    mark_value = Mark(ocena)
    if student_id not in marks_storage:
        marks_storage[student_id] = []
    marks_storage[student_id].append(mark_value)
    return {"message": "Ocena została dodana."}

@router.get("/{student_id}/marks")
async def get_marks(student_id: int):
    if student_id not in marks_storage:
        raise HTTPException(status_code=404, detail="Student ID not found")
    return {"marks": marks_storage[student_id]}

@router.get("/", status_code=200)
async def read_students():
    return {"Studenci": students}

@router.get("/{student_id}")
async def read_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student_id, "student": students[student_id]}
