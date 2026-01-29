from fastapi import APIRouter
from database import SessionLocal
from models import State, City, HeritageSite

router = APIRouter(prefix="/admin")

@router.get("/sites")
def get_all_sites():
    db = SessionLocal()
    sites = db.query(HeritageSite).all()
    result = []
    for s in sites:
        city = db.query(City).filter(City.id == s.city_id).first()
        state = db.query(State).filter(State.id == city.state_id).first()
        result.append({
            "id": s.id,
            "name": s.name,
            "category": s.category,
            "city": city.name,
            "state": state.name
        })
    db.close()
    return result


@router.post("/add-site")
def add_site(data: dict):
    db = SessionLocal()

    state = db.query(State).filter(State.name == data["state"]).first()
    city = db.query(City).filter(City.name == data["city"]).first()

    if not city:
        city = City(name=data["city"], state_id=state.id)
        db.add(city)
        db.commit()

    site = HeritageSite(
        name=data["name"],
        category=data["category"],
        city_id=city.id
    )

    db.add(site)
    db.commit()
    db.close()

    return {"message": "Site added successfully"}


@router.delete("/delete-site/{site_id}")
def delete_site(site_id: int):
    db = SessionLocal()
    site = db.query(HeritageSite).filter(HeritageSite.id == site_id).first()
    if site:
        db.delete(site)
        db.commit()
    db.close()
    return {"message": "Site deleted"}
