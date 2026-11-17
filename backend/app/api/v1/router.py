from fastapi import APIRouter
from app.api.v1 import auth, warehouse, fleet, tasks, twin, routing, simulation, catalog, orders, allocation, scenarios, audit, ws

api_router = APIRouter()
for module in (auth, warehouse, fleet, tasks, twin, routing, simulation, catalog, orders, allocation, scenarios, audit, ws):
    api_router.include_router(module.router)
