import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database import init_db
from routers import auth, recipes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # On Vercel, init_db() runs every time a "Cold Start" occurs.
    # SQLModel's create_all() is safe to run multiple times.
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "https://special-goggles-r4qjq6gwv67g3p4-3000.app.github.dev/",
    "https://recipe-4sku.vercel.app",
    "https://recipe-4sku-nl5xyu85j-atomizers-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(recipes.router)

@app.get("/")
def read_root():
    return {"status": "online", "message": "Recipe API is active"}