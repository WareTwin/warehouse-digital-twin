from fastapi import APIRouter

from app.core.security import generate_demo_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/demo-token")
def demo_token():
    """Development-only token generator. Replace with OIDC/JWT auth before deployment."""
    return {"access_token": generate_demo_token(), "token_type": "bearer", "development_only": True}
