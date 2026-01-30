from fastapi import FastAPI
from app.routes.auth import users

app = FastAPI()
app.include_router(users.router)