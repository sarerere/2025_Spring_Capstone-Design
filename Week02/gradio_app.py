import gradio as gr
import requests

def predict(sepal_length, sepal_width):
    response = requests.post("http://127.0.0.1:8000/predict", json={"sepal_length": sepal_length, "sepal_width": sepal_width})
    return response.json()["prediction"]

iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Slider(minimum=4.0, maximum=8.0, value=5.0, label="Sepal Length"),
        gr.Slider(minimum=2.0, maximum=4.5, value=3.0, label="Sepal Width")
    ],
    outputs="text",
    title="Iris Binary Classifier",
    description="Enter sepal length and sepal width to predict the Iris species."
)

iface.launch()