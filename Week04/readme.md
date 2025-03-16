팀 과제 : CRUD 게시판을 만들어라(MVC 구조)

- MVC(Model-View-Controller) 구조
    MVC는 소프트웨어 개발에서 애플리케이션을 3 개의 역할로 분리하는 아키텍처 패턴


########  파일 작동 매커니즘  ############

** POST 방식 POST /classes/이 작동을 따라가 보면서 이해

1. main.py
- FastAPI 애플리케이션의 진입점으로, API 엔드포인트를 정의
- FastAPI 인스턴스를 생성하고 API 제목을 설정
    @app.on_event("startup"): 앱 시작 시 데이터베이스 초기화를 수행
    Class API 엔드포인트:
        POST /classes/: 새 학급 생성
        GET /classes/{class_id}: 특정 학급 조회
        GET /classes/: 모든 학급 목록 조회
    Student API 엔드포인트:
        POST /students/: 새 학생 생성
        GET /students/{student_id}: 특정 학생 조회
        GET /classes/{class_id}/students/: 특정 학급의 학생 목록 조회
        GET /classes/{class_id}/with-students/: 특정 학급과 그에 속한 학생들을 함께 조회

각 엔드포인트는 적절한 응답 모델을 지정하고, 오류 처리를 포함

2. models.py
- 데이터 모델을 정의 담당
- Pydantic BaseModel을 상속받아 데이터 검증과 직렬화를 쉽게 처리
- Class 모델: 학급 정보 (ClassBase, ClassCreate, ClassResponse)
- Student 모델: 학생 정보 (StudentBase, StudentCreate, StudentResponse)
- 각 모델은 단계별로 사용
    Base: 기본 필드 정의
    Create: API 생성 요청에 사용
    Response: API 응답에 사용 (ID 포함)
    ClassWithStudents 모델은 학급과 그에 속한 학생들을 함께 반환할 때 사용
    orm_mode = True 설정은 ORM 객체와의 호환성을 위한 것

3. database.py
- 데이터베이스 연결과 초기화를 담당
- SQLite 데이터베이스를 사용 (school.db).
    init_db() 함수는 애플리케이션 시작 시 두 개의 테이블을 생성
- DB 설계
    classes: 학급 정보 저장 (id, name, description)
    students: 학생 정보 저장 (id, name, class_id)
        Primary & Foreign Key외래 키 관계: 학생 테이블의 class_id는 classes 테이블의 id를 참조

4. crud.py
- 데이터베이스 CRUD(Create, Read, Update, Delete) 연산(Operation)을 담당
- get_connection(): 데이터베이스 연결을 생성
    Class CRUD 함수:
        create_class(): 새 학급 생성
        get_class(): ID로 특정 학급 조회
        get_classes(): 모든 학급 목록 조회

    Student CRUD 함수:
        create_student(): 새 학생 생성
        get_student(): ID로 특정 학생 조회
        get_students_by_class(): 특정 학급에 속한 학생들 조회
- 각 함수는 SQL 쿼리를 실행하고 결과를 Pydantic 모델로 변환하여 반환

5. schema.py
- 이 파일은 별도의 스키마 정의를 포함하지만, 현재 시스템에서는 직접 사용되지 않습니다. 대신 models.py가 스키마 역할을 같이 수행
- UserBase, UserCreate, UserResponse 클래스를 정의하고 있지만, 이는 현재 구현된 class/student 시스템과는 무관
- 이 파일은 예제나 확장을 위한 참조용


############  전체 작동 흐름  ############### 
    애플리케이션이 시작되면 database.init_db()가 실행되어 필요한 테이블을 생성하 ㄴ후
    클라이언트가 API 엔드포인트에 요청을 보내면
    main.py의 라우트 핸들러가 요청을 받아 적절한 crud.py 함수를 호출하며
    crud.py는 데이터베이스 연결을 생성하고 SQL 쿼리를 실행하고
    결과 데이터는 models.py에 정의된 Pydantic 모델로 변환하여
    FastAPI는 이 Pydantic 모델을 자동으로 JSON으로 직렬화하여 클라이언트에 응답

---> FastAPI를 사용한 MVC 패턴의 구현 방식
        Model: models.py (데이터 구조 정의)
        View: FastAPI의 응답 모델 (JSON 변환)
        Controller: main.py의 라우트 핸들러와 crud.py의 함수들

이 구조는 관심사 분리를 잘 유지하면서도 간결한 코드 베이스를 제공하여 유지보수에 good
