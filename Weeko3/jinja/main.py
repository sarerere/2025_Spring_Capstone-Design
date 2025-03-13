# app.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

# 정적 파일 경로 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 경로 설정
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/bs4", response_class=HTMLResponse)
async def read_bs4_doc(request: Request):
    return templates.TemplateResponse("bs4_doc.html", {"request": request})

@app.get("/boots", response_class=HTMLResponse)
async def read_bootstra_doc(request: Request):
    return templates.TemplateResponse("bootstrap_doc.html", {"request": request})