from fastapi import APIRouter

from app.schemas.warehouse import WarehouseCreate

router = APIRouter(prefix="/warehouses", tags=["warehouses"])

@router.post("", status_code=201)
def create_warehouse(payload: WarehouseCreate):
    return {"id": 1, **payload.model_dump(), "note": "Starter endpoint; persistence wiring is a follow-up task."}

@router.get("")
def list_warehouses():
    return {"items": []}
