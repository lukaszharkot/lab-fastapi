from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)

def test_get_students():
    response = client.get("/")
    assert response.status_code ==200

def test_create_student_success():
    student_data = {"first_name": "Jan", "last_name": "Kowalski"}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 200
  
def test_create_student_failure():
    student_data = {"first_name": "Jan"}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 422

def test_create_and_get_students():
    students_data = [
        {"first_name": "Jan", "last_name": "Kowalski"},
        {"first_name": "Ola", "last_name": "Krawczyk"},
        {"first_name": "Maciej", "last_name": "Wilk"}
    ]
    for student_data in students_data:
        response = client.post("/students/", json=student_data)
        assert response.status_code == 200
    response = client.get("/students/")
 
@pytest.fixture(autouse=True)
def delete_all_students():
    for student, key in enumerate(client.get("/students").json()):
        client.delete(f"/students/{key}")