from pydantic import BaseModel, Field

class AGVRead(BaseModel):
    id: int
    code: str
    status: str
    x: int
    y: int
    model_config = {"from_attributes": True}
