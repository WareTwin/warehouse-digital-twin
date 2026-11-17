from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("")
def list_items():
    return {"items": [], "status": "starter"}
