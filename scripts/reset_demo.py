"""Destructive local-demo reset helper. Never point this at shared/production data."""
import os
import sys
from pathlib import Path

if os.getenv("APP_ENV", "development") != "development":
    raise SystemExit("Refusing reset: APP_ENV must be development")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app.db.base import Base
from app.db.session import engine
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("Local demo schema reset.")
