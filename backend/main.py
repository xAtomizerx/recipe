from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, select, Session
from database import init_db, get_session, engine
from models import Recipe, RecipeBase
from routers import auth, recipes
from contextlib import asynccontextmanager
import uvicorn

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Startup: Initialize the database (create tables)
    init_db()
    print("Database connected and tables created.")
    yield
    # 2. Shutdown: Logic to run when the server stops
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

# CORS Configuration
origins = [
    "http://localhost:3000",
    "https://recipe-4sku-nl5xyu85j-atomizers-projects.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers for auth and recipes
app.include_router(auth.router)
app.include_router(recipes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)