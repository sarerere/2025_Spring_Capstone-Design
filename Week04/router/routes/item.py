# from fastapi import APIRouter
# from pydantic import BaseModel

# router = APIRouter(prefix="/item", tags=["item"])

# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @router.get("/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @router.post("/")
# async def create_item(item: Item):
#     return item

# @router.put("/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "item": item}

# main.py
from fastapi import FastAPI, APIRouter

app = FastAPI()

# 라우터 생성
router = APIRouter(prefix="/items", tags=["items"])

# 라우터에 경로 추가
@router.get("/")
def get_items():
    return [{"id": 1, "name": "컴퓨터"}, {"id": 2, "name": "휴대폰"}]

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "예시 아이템"}

# 메인 앱에 라우터 포함시키기
app.include_router(router)

# 메인 앱 경로
@app.get("/")
def read_root():
    return {"message": "안녕하세요!"}