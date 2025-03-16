from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .crud import get_user, get_users, get_user_by_email, create_user, create_user_item, get_items

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", status_code=201)
def create_user_endpoint(email: str, password: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, email=email, password=password)

@app.get("/users/")
def read_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}")
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/items/", status_code=201)
def create_item_for_user_endpoint(user_id: int, title: str, description: str, db: Session = Depends(get_db)):
    return create_user_item(db=db, title=title, description=description, owner_id=user_id)

@app.get("/items/")
def read_items_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_items(db, skip=skip, limit=limit)
