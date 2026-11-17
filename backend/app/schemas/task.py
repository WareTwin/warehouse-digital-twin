from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    payload: dict = Field(default_factory=dict)

class TaskRead(BaseModel):
    id: int
    title: str
    status: str
    payload: dict
    model_config = {"from_attributes": True}
