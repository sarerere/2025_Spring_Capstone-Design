import sqlite3

# school.db 파일 생성
# classes, students 테이블 생성
DATABASE_URL = "school.db"

def init_db():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # 클래스 테이블 생성
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        description TEXT
    )
    ''')
    
    # 학생 테이블 생성
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        class_id INTEGER,
        FOREIGN KEY (class_id) REFERENCES classes (id)
    )
    ''')
    
    conn.commit()
    conn.close()