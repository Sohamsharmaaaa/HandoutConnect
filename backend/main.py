from fastapi import FastAPI
from backend.routes import auth

app = FastAPI()

# Include authentication routes
app.include_router(auth.router, prefix="/auth")

# Root endpoint
@app.get("/")
def root():
    return {"message": "HandoutConnect API is running"}
