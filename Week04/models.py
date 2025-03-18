from pydantic import BaseModel
from typing import Optional, List

'''
- Pydantic 모델은 데이터 검증 및 직렬화(Serialization) 를 담당
- 이를 통해 API 요청(Request)과 응답(Response)에서 사용할 데이터 구조를 명확하게 정의
- FastAPI에서 사용하는 모델은 Pydantic의 BaseModel을 상속받아 정의
'''

'''
- BaseModel → Pydantic에서 제공하는 데이터 모델의 기본 클래스
- Optional → 해당 필드가 선택적으로 들어올 수 있도록 설정
- List → 리스트 형태의 데이터를 표현할 때 사용
= orm_mode = True → ORM(SQLAlchemy 등)과의 호환을 위해 사용
'''

# 클래스 모델
class ClassBase(BaseModel):
    name: str
    description: Optional[str] = None

class ClassCreate(ClassBase):
    pass

class ClassResponse(ClassBase):
    id: int
    
    class Config:
        orm_mode = True

# 학생 모델
class StudentBase(BaseModel):
    name: str
    class_id: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    
    class Config:
        orm_mode = True

# 클래스와 학생 목록 반환용 모델
'''
- ClassResponse(기존 강의 응답)에 students 필드를 추가
- students → List[StudentResponse] 형식으로, 학생 리스트 포함
- 기본값은 [](빈 리스트)로 설정.
'''

class ClassWithStudents(ClassResponse):
    students: List[StudentResponse] = []
    
'''
아래처럼 특정 강의에 속한 학생 목록을 함께 응답할 수 있도록 ClassWithStudents 모델을 정의

{
    "id": 1,
    "name": "캡스톤디자인",
    "description": "MVC 패턴을 이용한 웹 서비스 개발",
    "students": [
        {
            "id": 101,
            "name": "안영진",
            "class_id": 1
        },
        {
            "id": 102,
            "name": "정현중",
            "class_id": 1
        }
    ]
}

'''


'''
모델명	                   용도	                      필드
-------------------------------------------------------------------------------------------------
ClassBase	        강의 정보 기본 모델	        name, description
ClassCreate	        강의 생성 요청	            ClassBase 그대로 사용
ClassResponse	    강의 응답 모델	            id 추가 (orm_mode=True)
StudentBase	        학생 기본 정보	            name, class_id
StudentCreate	    학생 생성 요청	            StudentBase 그대로 사용
StudentResponse	    학생 응답 모델	            id 추가 (orm_mode=True)
ClassWithStudents	특정 강의의 학생 목록 반환   ClassResponse + students: List[StudentResponse]
-------------------------------------------------------------------------------------------------
'''