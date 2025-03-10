from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the pre-trained model
model = joblib.load("iris_model.pkl")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float

@app.post("/predict")
def predict(iris: IrisInput):
    data = [[iris.sepal_length, iris.sepal_width]]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}