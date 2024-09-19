from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sys import api_version
import uvicorn
from prediction import make_prediction

app = FastAPI()

class features(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    contact: str
    month: str
    day_of_week: str
    duration: float
    campaign: int
    pdays: int
    previous: int
    poutcome: str

@app.get("/")
def read_root():
       return {"message": "Long Term Deposit Prediction", "version": api_version}

@app.post("/predict/")
def predict_endpoint(client_data: features):
    try:
        prediction = make_prediction(client_data)
        return {"Prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

