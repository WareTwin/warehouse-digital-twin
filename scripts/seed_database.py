import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app.db.session import SessionLocal
from app.db.seed import seed_demo_data

with SessionLocal() as db:
    seed_demo_data(db)
print("Demo data seeded.")
