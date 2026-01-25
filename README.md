# Smart Heritage Trail

A full-stack web application that helps users explore heritage sites
based on state and city selection.

## Tech Stack
- Frontend: React.js
- Backend: FastAPI (Python)
- API Communication: Axios

## Features
- Select state and city
- Fetch heritage sites dynamically
- REST API powered backend
- Simple and clean UI

## API Endpoints
- GET /states
- GET /cities/{state}
- GET /sites/{state}/{city}

## How to Run the Project

### Backend
```bash
cd backend
python -m uvicorn main:app --reload
