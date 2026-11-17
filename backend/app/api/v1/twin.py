from fastapi import APIRouter
from app.services.twin import snapshot

router = APIRouter(prefix="/twin", tags=["digital twin"])

@router.get("/snapshot")
def get_snapshot():
    return snapshot()
