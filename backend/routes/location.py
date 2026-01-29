from fastapi import APIRouter
from database import SessionLocal
from models import State, City

router = APIRouter()

@router.get("/states")
def get_states():
    db = SessionLocal()
    states = db.query(State).all()
    db.close()
    return [s.name for s in states]

@router.get("/cities/{state}")
def get_cities(state: str):
    db = SessionLocal()
    st = db.query(State).filter(State.name == state).first()
    if not st:
        return []
    cities = db.query(City).filter(City.state_id == st.id).all()
    db.close()
    return [c.name for c in cities]
