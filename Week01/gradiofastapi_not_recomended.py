from typing import Union
import gradio as gr
import uvicorn
from fastapi import FastAPI
import threading

# FastAPI 앱 생성
app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hi sangoo'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Gradio 인터페이스
def process_item(item_id: int, query: str = None):
    """
    아이템 ID와 쿼리를 처리하는 함수
    """
    if query:
        return f"아이템 ID: {item_id}, 쿼리: {query}"
    return f"아이템 ID: {item_id}"

def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# 아이템 조회 시스템")
        
        with gr.Row():
            item_id_input = gr.Number(label="아이템 ID", value=0)
            query_input = gr.Textbox(label="쿼리(선택사항)")
            
        submit_btn = gr.Button("조회하기")
        output = gr.Textbox(label="결과")
        
        submit_btn.click(
            fn=process_item,
            inputs=[item_id_input, query_input],
            outputs=output
        )
    
    return demo

# FastAPI 서버 실행 함수
def run_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    # FastAPI 서버를 별도 스레드에서 실행
    print("FastAPI 서버를 시작합니다...")
    fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
    fastapi_thread.start()
    
    # Gradio 인터페이스 실행
    print("Gradio 서버를 시작합니다...")
    demo = create_interface()
    demo.launch(share=True)