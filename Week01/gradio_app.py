import gradio as gr

def process_item(item_id: int, query: str = None):
    """
    아이템 ID와 쿼리를 처리하는 함수
    """
    if query:
        return f"아이템 ID: {item_id}, 쿼리: {query}"
    return f"아이템 ID: {item_id}"

# Gradio 인터페이스 생성
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

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=True)    # share=True를 추가하여 공개 URL 생성
    print("서버가 실행되었습니다. 브라우저를 확인해주세요.")