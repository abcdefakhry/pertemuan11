from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI(
    title="Obesity Prediction API",
    version="1.0.0"
)

try:
    model = joblib.load("model.pkl")
    print("Model berhasil di-load")
except Exception as e:
    print("Gagal load model:", e)
    model = None

class ObesityData(BaseModel):
    height: float
    weight: float
    age: int

@app.get("/health")
def health_check():

    if model is None:
        return {
            "status": "error",
            "message": "Model belum tersedia"
        }

    return {
        "status": "success",
        "message": "Python ML Service aktif"
    }

@app.get("/")
def home():
    return {
        "message": "Obesity Prediction API"
    }

@app.post("/predict")
def predict(data: ObesityData):

    try:

        if model is None:
            raise HTTPException(
                status_code=500,
                detail="Model tidak tersedia"
            )

        prediction = model.predict([[
            data.height,
            data.weight,
            data.age
        ]])

        return {
            "status": "success",
            "prediction": prediction[0]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
