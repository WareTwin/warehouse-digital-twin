from fastapi import APIRouter

router = APIRouter(prefix="/allocation", tags=["allocation"])

@router.get("")
def list_items():
    return {"items": [], "status": "starter"}
