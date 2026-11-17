from datetime import datetime, timezone

def snapshot() -> dict:
    return {"timestamp": datetime.now(timezone.utc).isoformat(), "warehouse": None, "agvs": [], "tasks": []}
