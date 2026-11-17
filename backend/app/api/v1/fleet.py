from fastapi import APIRouter

router = APIRouter(prefix="/fleet", tags=["fleet"])

@router.get("/agvs")
def list_agvs():
    return {"items": []}
