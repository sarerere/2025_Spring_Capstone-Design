from fastapi import FastAPI, HTTPException
from typing import List

import database
from models import ClassCreate, ClassResponse, StudentCreate, StudentResponse, ClassWithStudents
import crud

app = FastAPI(title="School API")

# FastAPI가 시작될 때 실행되는 이벤트 핸들러
# database 파일의 init_db 함수를 호출하여 데이터베이스를 생성 초기화
# school.db 파일이 생성되고 classes, students 테이블이 생성됨
@app.on_event("startup")
def startup_db_client():
    database.init_db()

# 1. 클래스 API 엔드포인트

'''
- HTTP POST 요청을 처리하여 새로운 클래스를 생성하는 API
- @app.post("/classes/") → POST 요청을 받을 URL을 지정
- response_model=ClassResponse → 응답 데이터의 모델을 지정하여 API 응답 형식을 정의
- status_code=201 → 요청이 성공하면 HTTP 201 Created 상태 코드를 반환
- class_data: models.py의 ClassCreate → 클라이언트에서 받은 요청 데이터를 FastAPI 모델(ClassCreate)로 변환
- return: crud파일의 create_class() 함수를 호출하여  → 새로운 클래스를 데이터베이스에 추가
'''
@app.post("/classes/", response_model=ClassResponse, status_code=201)
def create_class(class_data: ClassCreate):
    return crud.create_class(name=class_data.name, description=class_data.description)


@app.get("/classes/{class_id}", response_model=ClassResponse)
def get_class(class_id: int):
    db_class = crud.get_class(class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class

@app.get("/classes/", response_model=List[ClassResponse])
def get_classes():
    return crud.get_classes()

# 2. 학생 API 엔드포인트

'''
- HTTP POST 요청을 처리하여 새로운 학생을 생성하는 API
- @app.post("/students/") → POST 요청을 받을 URL을 지정
- response_model=StudentResponse → 응답 데이터의 모델을 지정하여 API 응답 형식을 정의
- status_code=201 → 요청이 성공하면 HTTP 201 Created 상태 코드를 반환
- student_data: models.py의 StudentCreate → 클라이언트에서 받은 요청 데이터를 FastAPI 모델(StudentCreate)로 변환
- return: crud파일의 create_student() 함수를 호출하여  → 새로운 학생을 데이터베이스에 추가
'''
@app.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(student_data: StudentCreate):
    return crud.create_student(name=student_data.name, class_id=student_data.class_id)

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    db_student = crud.get_student(student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.get("/classes/{class_id}/students/", response_model=List[StudentResponse])
def get_students_by_class(class_id: int):
    db_class = crud.get_class(class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return crud.get_students_by_class(class_id)

@app.get("/classes/{class_id}/with-students/", response_model=ClassWithStudents)
def get_class_with_students(class_id: int):
    db_class = crud.get_class(class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    
    students = crud.get_students_by_class(class_id)
    return ClassWithStudents(
        id=db_class.id,
        name=db_class.name,
        description=db_class.description,
        students=students
    )

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)