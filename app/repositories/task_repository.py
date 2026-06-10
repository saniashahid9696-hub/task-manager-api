from sqlalchemy.orm import Session
from app.repositories.base import TaskModel
from app.domain.schemas import TaskCreate

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_user(self, user_id: str):
        return self.db.query(TaskModel).filter(TaskModel.owner_id == user_id).all()

    def create(self, task: TaskCreate, user_id: str):
        db_task = TaskModel(**task.model_dump(), owner_id=user_id)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task