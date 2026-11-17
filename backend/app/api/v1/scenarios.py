from fastapi import APIRouter

router = APIRouter(prefix="/scenarios", tags=["scenarios"])

@router.get("")
def list_items():
    return {"items": [], "status": "starter"}
