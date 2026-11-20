import hashlib
import secrets


def hash_token(token: str) -> str:
    """Return a SHA-256 digest for token lookup; never log the raw token."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()

def generate_demo_token() -> str:
    """Generate a cryptographically secure random token for local experiments."""
    return secrets.token_urlsafe(32)
