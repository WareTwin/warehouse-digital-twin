from pydantic import BaseModel, Field

class WarehouseCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    width: int = Field(default=20, ge=1, le=500)
    height: int = Field(default=20, ge=1, le=500)

class WarehouseRead(WarehouseCreate):
    id: int
    model_config = {"from_attributes": True}
