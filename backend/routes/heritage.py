from fastapi import APIRouter
from typing import List

router = APIRouter()

HERITAGE_DATA = {
    "Bhopal": [
        {"name": "Upper Lake", "category": "Nature"},
        {"name": "Taj-ul-Masajid", "category": "Architecture"},
        {"name": "Bhimbetka Rock Shelters", "category": "History"}
    ],
    "Indore": [
        {"name": "Rajwada Palace", "category": "Architecture"},
        {"name": "Lal Bagh Palace", "category": "History"}
    ]
}

@router.post("/heritage/{city}")
def get_heritage(city: str, interests: List[str]):
    sites = HERITAGE_DATA.get(city, [])
    if not interests:
        return sites
    return [s for s in sites if s["category"] in interests]
