from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "jaipur_sites.csv")

data = pd.read_csv(DATA_PATH)

@app.get("/")
def home():
    return {"message": "Smart Heritage API running"}

@app.get("/trail")
def get_trail(interest: str):
    result = data[data["category"] == interest]
    return result.to_dict()
