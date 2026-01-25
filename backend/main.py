from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# 1️⃣ Create app FIRST
app = FastAPI()

# 2️⃣ Add CORS AFTER app is created
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ Your data
heritage_data = {
    "Madhya Pradesh": {
        "Bhopal": ["Sanchi Stupa", "Upper Lake"],
        "Khajuraho": ["Western Group of Temples"],
        "Gwalior": ["Gwalior Fort"],
    }
}

# 4️⃣ Routes
@app.get("/states")
def get_states():
    return list(heritage_data.keys())


@app.get("/cities/{state}")
def get_cities(state: str):
    if state not in heritage_data:
        raise HTTPException(status_code=404, detail="State not found")
    return list(heritage_data[state].keys())


@app.get("/sites/{state}/{city}")
def get_sites(state: str, city: str):
    if state not in heritage_data:
        raise HTTPException(status_code=404, detail="State not found")
    if city not in heritage_data[state]:
        raise HTTPException(status_code=404, detail="City not found")
    return heritage_data[state][city]
# 5️⃣ Run the app with: uvicorn backend.main:app --reload