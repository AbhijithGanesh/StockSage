from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from model import create_model, predict_values

class Model(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float

app = FastAPI()

@app.post("/predict")
def predict_http(data: Model):
    model = create_model()
    model.load_weights("model_weights.h5")
    df = pd.DataFrame([data])   
    return predict_values(model, df)
