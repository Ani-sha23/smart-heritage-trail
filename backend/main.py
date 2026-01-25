from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote

# ---------------- APP ----------------
app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DATA ----------------
heritage_data = {
    "Madhya Pradesh": {

        "Gwalior": [
            {"name": "Gwalior Fort", "desc": "Historic hill fort with palaces and temples."},
            {"name": "Jai Vilas Palace", "desc": "Grand palace showcasing European architecture."}
        ],

        "Bhopal": [
            {"name": "Upper Lake", "desc": "Large scenic lake and major attraction."},
            {"name": "Van Vihar National Park", "desc": "National park inside the city."},
            {"name": "Taj-ul-Masajid", "desc": "One of the largest mosques in India."}
        ],

        "Indore": [
            {"name": "Rajwada Palace", "desc": "Historic palace of the Holkar dynasty."},
            {"name": "Lal Bagh Palace", "desc": "Royal palace with European-style interiors."}
        ],

        "Ujjain": [
            {"name": "Mahakaleshwar Jyotirlinga", "desc": "One of the 12 Jyotirlingas of Lord Shiva."},
            {"name": "Ram Ghat", "desc": "Sacred ghat on Shipra river."}
        ],

        "Khajuraho": [
            {"name": "Western Group of Temples", "desc": "UNESCO heritage temples with intricate carvings."},
            {"name": "Eastern Group of Temples", "desc": "Jain temples of historical importance."}
        ],

        "Sanchi": [
            {"name": "Sanchi Stupa", "desc": "Ancient Buddhist monument and UNESCO site."}
        ],

        "Orchha": [
            {"name": "Orchha Fort", "desc": "Fort complex with palaces and temples."},
            {"name": "Ram Raja Temple", "desc": "Unique temple where Lord Ram is worshipped as king."}
        ],

        "Jabalpur": [
            {"name": "Bhedaghat Marble Rocks", "desc": "Marble cliffs along Narmada river."},
            {"name": "Dhuandhar Falls", "desc": "Waterfall known for its misty appearance."}
        ],

        "Mandu": [
            {"name": "Jahaz Mahal", "desc": "Ship-shaped palace between two lakes."},
            {"name": "Hindola Mahal", "desc": "Swinging palace with sloping walls."}
        ],

        "Chhindwara": [
            {"name": "Pench National Park", "desc": "Tiger reserve that inspired The Jungle Book."}
        ],

        "Satna": [
            {"name": "Chitrakoot", "desc": "Spiritual town associated with Lord Rama."}
        ],

        "Rewa": [
            {"name": "Rewa Fort", "desc": "Historic fort and royal residence."},
            {"name": "White Tiger Safari", "desc": "Safari park famous for white tigers."}
        ],

        "Sehore": [
            {"name": "Bhimbetka Rock Shelters", "desc": "Prehistoric cave paintings and UNESCO site."}
        ],

        "Hoshangabad": [
            {"name": "Pachmarhi", "desc": "Hill station and biosphere reserve."}
        ],

        "Datia": [
            {"name": "Datia Palace", "desc": "Seven-storied palace built without iron or wood."}
        ],

        "Shivpuri": [
            {"name": "Madhav National Park", "desc": "Wildlife park with lakes and forests."}
        ]
    }
}

# ---------------- ROUTES ----------------

@app.get("/")
def root():
    return {"message": "Smart Heritage Trail API running"}

@app.get("/states")
def get_states():
    return list(heritage_data.keys())

@app.get("/cities/{state}")
def get_cities(state: str):
    state = unquote(state)
    if state not in heritage_data:
        raise HTTPException(status_code=404, detail="State not found")
    return list(heritage_data[state].keys())

@app.get("/sites/{state}/{city}")
def get_sites(state: str, city: str):
    state = unquote(state)
    city = unquote(city)

    if state not in heritage_data:
        raise HTTPException(status_code=404, detail="State not found")

    if city not in heritage_data[state]:
        raise HTTPException(status_code=404, detail="City not found")

    return heritage_data[state][city]
# ---------------- RUN ----------------
