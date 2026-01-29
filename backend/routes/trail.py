from fastapi import APIRouter
from typing import List
from database import SessionLocal
from models import City, HeritageSite

router = APIRouter()

@router.post("/generate-trail/{city}")
def generate_trail(city: str, interests: List[str]):
    db = SessionLocal()
    city_obj = db.query(City).filter(City.name == city).first()

    if not city_obj:
        return {"city": city, "sites": []}

    query = db.query(HeritageSite).filter(
        HeritageSite.city_id == city_obj.id
    )

    if interests:
        query = query.filter(HeritageSite.category.in_(interests))

    sites = query.limit(5).all()
    db.close()

    return {
        "city": city,
        "total_sites": len(sites),
        "sites": [
            {"name": s.name, "category": s.category}
            for s in sites
        ]
    }
