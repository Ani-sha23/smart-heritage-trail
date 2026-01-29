from database import SessionLocal
from models import State, City, HeritageSite

db = SessionLocal()

# Clear old data
db.query(HeritageSite).delete()
db.query(City).delete()
db.query(State).delete()
db.commit()

mp = State(name="Madhya Pradesh")
rj = State(name="Rajasthan")
db.add_all([mp, rj])
db.commit()

cities = {
    "Madhya Pradesh": [
        ("Bhopal", [
            ("Upper Lake", "Nature"),
            ("Taj-ul-Masajid", "Architecture"),
            ("State Museum", "Museum")
        ]),
        ("Indore", [
            ("Rajwada Palace", "Architecture"),
            ("Lal Bagh Palace", "Architecture"),
            ("Central Museum Indore", "Museum")
        ])
    ],
    "Rajasthan": [
        ("Jaipur", [
            ("Amber Fort", "Fort"),
            ("Hawa Mahal", "Architecture"),
            ("City Palace", "Museum")
        ]),
        ("Udaipur", [
            ("Lake Pichola", "Nature"),
            ("City Palace Udaipur", "Museum")
        ])
    ]
}

for state in [mp, rj]:
    for city_name, sites in cities[state.name]:
        city = City(name=city_name, state_id=state.id)
        db.add(city)
        db.commit()

        for site_name, category in sites:
            db.add(HeritageSite(
                name=site_name,
                category=category,
                city_id=city.id
            ))
        db.commit()

db.close()
print("Data seeded successfully")
