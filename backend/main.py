from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import auth, users, donations

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allows OPTIONS method for preflight requests
    allow_headers=["*"],
)

# ✅ Register API routes
app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(donations.router, prefix="/donations")

@app.get("/")
def root():
    return {"message": "HandoutConnect API is running"}
