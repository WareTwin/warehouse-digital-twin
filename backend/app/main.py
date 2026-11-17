from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router

app = FastAPI(title=settings.app_name, version="0.1.0", description="Warehouse Digital Twin API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok", "service": settings.app_name, "environment": settings.app_env}

@app.get("/", include_in_schema=False)
def root():
    return {"message": "WareTwin API", "docs": "/docs", "health": "/health"}
