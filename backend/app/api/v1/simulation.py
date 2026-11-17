from fastapi import APIRouter

router = APIRouter(prefix="/simulation", tags=["simulation"])

@router.get("")
def list_items():
    return {"items": [], "status": "starter"}
