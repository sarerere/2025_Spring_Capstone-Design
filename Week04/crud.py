import sqlite3
from models import ClassResponse, StudentResponse
from database import DATABASE_URL

# 데이터베이스 연결 함수
def get_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

# 클래스 CRUD 함수
def create_class(name: str, description: str = None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO classes (name, description) VALUES (?, ?)",
        (name, description)
    )
    conn.commit()
    class_id = cursor.lastrowid
    conn.close()
    return ClassResponse(id=class_id, name=name, description=description)

def get_class(class_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes WHERE id = ?", (class_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return ClassResponse(id=row['id'], name=row['name'], description=row['description'])
    return None

def get_classes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes")
    rows = cursor.fetchall()
    conn.close()
    
    return [ClassResponse(id=row['id'], name=row['name'], description=row['description']) for row in rows]

# 학생 CRUD 함수
def create_student(name: str, class_id: int = None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, class_id) VALUES (?, ?)",
        (name, class_id)
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    
    return StudentResponse(id=student_id, name=name, class_id=class_id)

def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return StudentResponse(id=row['id'], name=row['name'], class_id=row['class_id'])
    return None

def get_students_by_class(class_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE class_id = ?", (class_id,))
    rows = cursor.fetchall()
    conn.close()
    
    return [StudentResponse(id=row['id'], name=row['name'], class_id=row['class_id']) for row in rows]