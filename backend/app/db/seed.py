from sqlalchemy.orm import Session

from app.db.models import AGV, Warehouse


def seed_demo_data(db: Session) -> None:
    if not db.query(Warehouse).first():
        db.add(Warehouse(name="Demo Warehouse", width=20, height=12))
    if not db.query(AGV).first():
        db.add_all([
            AGV(code="AGV-001", status="idle", x=1, y=1),
            AGV(code="AGV-002", status="charging", x=5, y=2),
        ])
    db.commit()
