from typing import Annotated
from fastapi import Header, HTTPException, status

def require_demo_auth(authorization: Annotated[str | None, Header()] = None) -> str:
    """Placeholder auth dependency. Replace with verified JWT/OIDC validation before deployment."""
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token.strip():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid bearer token")
    return token
