from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int):
    query = "SELECT * FROM users WHERE id = :id"
    result = db.execute(query, {"id": user_id}).fetchone()
    return dict(result) if result else None

def get_user_by_email(db: Session, email: str):
    query = "SELECT * FROM users WHERE email = :email"
    result = db.execute(query, {"email": email}).fetchone()
    return dict(result) if result else None

def get_users(db: Session, skip: int = 0, limit: int = 100):
    query = "SELECT * FROM users LIMIT :limit OFFSET :skip"
    results = db.execute(query, {"limit": limit, "skip": skip}).fetchall()
    return [dict(row) for row in results]

def create_user(db: Session, email: str, password: str):
    query = "INSERT INTO users (email, hashed_password, is_active) VALUES (:email, :hashed_password, :is_active)"
    db.execute(query, {"email": email, "hashed_password": password + "notreallyhashed", "is_active": True})
    db.commit()
    return get_user_by_email(db, email)

def get_items(db: Session, skip: int = 0, limit: int = 100):
    query = "SELECT * FROM items LIMIT :limit OFFSET :skip"
    results = db.execute(query, {"limit": limit, "skip": skip}).fetchall()
    return [dict(row) for row in results]

def create_user_item(db: Session, title: str, description: str, owner_id: int):
    query = "INSERT INTO items (title, description, owner_id) VALUES (:title, :description, :owner_id)"
    db.execute(query, {"title": title, "description": description, "owner_id": owner_id})
    db.commit()
    return db.execute("SELECT * FROM items WHERE id = (SELECT last_insert_rowid())").fetchone()
