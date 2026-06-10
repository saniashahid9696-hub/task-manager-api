from fastapi import FastAPI
from app.api import tasks, auth
from app.repositories.base import init_db

# Connect to DB and create tables
init_db()

app = FastAPI(title="Task Manager API")

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager is live"}