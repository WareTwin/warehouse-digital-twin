from datetime import UTC, datetime


def snapshot() -> dict:
    return {"timestamp": datetime.now(UTC).isoformat(), "warehouse": None, "agvs": [], "tasks": []}
