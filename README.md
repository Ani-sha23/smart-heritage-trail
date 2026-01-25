# 🏛️ Smart Heritage Trail – MP

A full-stack web application to explore cultural heritage sites of Madhya Pradesh city-wise.

---

## ✨ Features
- City-wise heritage trail generator
- Google Maps integration
- Responsive modern UI
- FastAPI backend + React frontend
- Error handling & loading states

---

## 🛠️ Tech Stack
- Frontend: React, CSS
- Backend: FastAPI (Python)
- API calls: Axios

---

## 📡 API Endpoints
- GET /states
- GET /cities/{state}
- GET /sites/{state}/{city}

---

## ▶️ How to Run

### Backend
```bash
cd backend
python -m uvicorn main:app --reload
