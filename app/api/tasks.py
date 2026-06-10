from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repositories.base import SessionLocal
from app.repositories.task_repository import TaskRepository
from app.domain import schemas
from app.api.auth_deps import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Task])
def list_tasks(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    repo = TaskRepository(db)
    return repo.get_by_user(user)

@router.post("/", response_model=schemas.Task)
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    repo = TaskRepository(db)
    return repo.create(task, user)