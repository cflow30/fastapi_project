from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models 
from app.database import engine
from .routers import post, users, auth, votes
from .config import settings

# creating database without alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "welcome to my api!!!"}







