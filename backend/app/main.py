from fastapi import FastAPI
from app.routers import auth
from app.middleware.session import setup_session
app=FastAPI()
setup_session(app)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI app"}