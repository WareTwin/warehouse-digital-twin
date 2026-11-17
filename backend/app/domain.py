from enum import StrEnum

class AGVStatus(StrEnum):
    IDLE = "idle"
    ASSIGNED = "assigned"
    MOVING = "moving"
    CHARGING = "charging"
    OFFLINE = "offline"

class TaskStatus(StrEnum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
