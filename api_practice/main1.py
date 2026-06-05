from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    cls: str
    cgpa: float

students_db = {}

@app.get("/student/{student_id}")
def show_results(student_id: int):
    if student_id in students_db:
        return students_db[student_id]
    return {"error": "Student not found"}

@app.post("/student/{student_id}")
def create_student(student_id: int, student: Student):
    students_db[student_id] = student
    return {
        "message": "Student created ",
        "data": student
    }
"""
@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students_db:
        return {"error": "Student not found"}
    
    students_db[student_id] = student
    return {
        "message": "Student updated successfully",
        "data": student
    }
"""