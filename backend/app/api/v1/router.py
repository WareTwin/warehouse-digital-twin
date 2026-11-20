from fastapi import APIRouter

from app.api.v1 import (
    allocation,
    audit,
    auth,
    catalog,
    fleet,
    orders,
    routing,
    scenarios,
    simulation,
    tasks,
    twin,
    warehouse,
    ws,
)

api_router = APIRouter()
for module in (auth, warehouse, fleet, tasks, twin, routing, simulation, catalog, orders, allocation, scenarios, audit, ws):
    api_router.include_router(module.router)
