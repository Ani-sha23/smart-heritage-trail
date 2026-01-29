from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.location import router as location_router
from routes.trail import router as trail_router
from routes.digital_pass import router as pass_router
from routes.admin import router as admin_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(location_router)
app.include_router(trail_router)
app.include_router(pass_router)
app.include_router(admin_router)
