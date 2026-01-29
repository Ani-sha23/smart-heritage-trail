from fastapi import APIRouter
from fastapi.responses import FileResponse
import uuid
import qrcode
import os

router = APIRouter()

PASS_STORE = {}

QR_DIR = "qrcodes"
os.makedirs(QR_DIR, exist_ok=True)

@router.post("/create-pass")
def create_pass(trail: dict):
    pass_id = str(uuid.uuid4())

    PASS_STORE[pass_id] = trail

    qr_url = f"http://127.0.0.1:8000/pass/{pass_id}"

    img = qrcode.make(qr_url)
    img_path = f"{QR_DIR}/{pass_id}.png"
    img.save(img_path)

    return {
        "pass_id": pass_id,
        "qr_image": f"/qrcode/{pass_id}"
    }

@router.get("/pass/{pass_id}")
def get_pass(pass_id: str):
    return PASS_STORE.get(pass_id, {"error": "Invalid pass"})

@router.get("/qrcode/{pass_id}")
def get_qr(pass_id: str):
    path = f"{QR_DIR}/{pass_id}.png"
    if os.path.exists(path):
        return FileResponse(path, media_type="image/png")
    return {"error": "QR not found"}

