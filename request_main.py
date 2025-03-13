# Request 객체는 FastAPI에서 HTTP 요청 정보를 담고 있는 객체
# 클라이언트(브라우저, API 호출 등)가 서버로 보낸 요청의 메서드, 헤더, 본문, 쿼리 파라미터, 쿠키 등을 포함
# Request 객체는 기본적으로 템플릿 렌더링할 때 또는 요청 정보를 직접 분석할 때 필요

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    return {"method": request.method, "client": request.client}

@app.get("/client")
async def get_client_info(request: Request):
    return {"client_ip": request.client.host, "client_port": request.client.port}

@app.get("/items/{item_id}")
async def get_url_info(request: Request, item_id: int):
    return {
        "full_url": str(request.url),
        "base_url": str(request.base_url),
        "path_params": request.path_params,
        "query_params": request.query_params
    }
    
@app.get("/headers")
async def get_headers(request: Request):
    return {"headers": dict(request.headers)}

from fastapi import Form

@app.post("/submit")
async def submit_form(username: str = Form(...), age: int = Form(...)):
    return {
        "username": username,
        "age": age,
    }

@app.get("/cookies")
async def get_cookies(request: Request):
    return {"cookies": request.cookies}

from fastapi.responses import JSONResponse

@app.get("/custom-header")
async def custom_header():
    response = JSONResponse(content={"message": "Hello"})
    response.headers["X-Custom-Header"] = "My Custom Value"
    return response