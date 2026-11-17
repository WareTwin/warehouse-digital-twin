from fastapi import APIRouter

router = APIRouter(prefix="/audit", tags=["audit"])

@router.get("")
def list_items():
    return {"items": [], "status": "starter"}
