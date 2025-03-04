import gradio as gr
import requests

def process_item(item_id: int, query: str = None):
    """
    FastAPI 서버에 요청을 보내고 결과를 받아오는 함수
    """
    # FastAPI 서버 URL (main.py가 실행 중인 서버)
    base_url = "http://127.0.0.1:8000"
    
    try:
        if query:
            response = requests.get(f"{base_url}/items/{item_id}", params={"q": query})
        else:
            response = requests.get(f"{base_url}/items/{item_id}")
        
        if response.status_code == 200:
            result = response.json()
            return f"서버 응답: {result}"
        else:
            return f"서버 오류: {response.status_code}"
            
    except requests.ConnectionError:
        return "오류: FastAPI 서버가 실행 중인지 확인해주세요. (main.py를 먼저 실행해야 합니다)"
    except Exception as e:
        return f"오류 발생: {str(e)}"

def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# FastAPI 아이템 조회 시스템")
        gr.Markdown("### main.py 서버와 통신하는 클라이언트")
        
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

if __name__ == "__main__":
    print("Gradio 클라이언트를 시작합니다...")
    print("주의: main.py의 FastAPI 서버가 먼저 실행되어 있어야 합니다!")
    demo = create_interface()
    demo.launch(share=True)