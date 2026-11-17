from fastapi import APIRouter
from app.schemas.task import TaskCreate

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("")
def list_tasks():
    return {"items": []}

@router.post("", status_code=201)
def create_task(payload: TaskCreate):
    return {"id": 1, **payload.model_dump(), "status": "pending"}
