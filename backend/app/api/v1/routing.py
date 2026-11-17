from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.engines.contracts import Point
from app.engines.routing.bfs import find_path

router = APIRouter(prefix="/routing", tags=["routing"])

class RouteRequest(BaseModel):
    start: Point
    goal: Point
    blocked: list[Point] = []

@router.post("/bfs")
def route(payload: RouteRequest):
    try:
        result = find_path(set(payload.blocked), payload.start, payload.goal)
        return {"algorithm": result.algorithm, "cost": result.cost,
                "path": [p.__dict__ for p in result.path]}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
