from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 데이터 저장소 역할
items = []

# 데이터 모델 정의
class Item(BaseModel):
    id: int
    name: str
    description: str

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [item for item in items if item.id != item_id]
    return {"message": "Item deleted"}

# --------------- ngrok
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# import uvicorn
# from pyngrok import ngrok

# app = FastAPI()

# # 데이터 저장소 역할
# items = []

# # 데이터 모델 정의
# class Item(BaseModel):
#     id: int
#     name: str
#     description: str

# @app.post("/items/", response_model=Item)
# def create_item(item: Item):
#     items.append(item)
#     return item

# @app.get("/items/", response_model=List[Item])
# def read_items():
#     return items

# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: int):
#     for item in items:
#         if item.id == item_id:
#             return item
#     return {"error": "Item not found"}

# @app.put("/items/{item_id}", response_model=Item)
# def update_item(item_id: int, updated_item: Item):
#     for index, item in enumerate(items):
#         if item.id == item_id:
#             items[index] = updated_item
#             return updated_item
#     return {"error": "Item not found"}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     global items
#     items = [item for item in items if item.id != item_id]
#     return {"message": "Item deleted"}

# # ngrok 설정 및 실행
# # ngrok 설정 및 실행
# def start_ngrok():
#     # ngrok 인증 토큰 설정
#     ngrok.set_auth_token("Your ngrok API Key")
    
#     # ngrok 포트 설정 (FastAPI의 기본 포트는 8000)
#     port = 8000
    
#     # ngrok 터널 생성
#     public_url = ngrok.connect(port).public_url
#     print(f"ngrok 터널이 생성되었습니다: {public_url}")
    
#     # FastAPI 문서에 ngrok URL 추가
#     app.root_path = public_url