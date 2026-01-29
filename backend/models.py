from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey("states.id"))

class HeritageSite(Base):
    __tablename__ = "heritage_sites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))
