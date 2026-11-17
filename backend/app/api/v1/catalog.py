from fastapi import APIRouter

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.get("")
def list_items():
    return {"items": [], "status": "starter"}
