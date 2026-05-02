from datetime import datetime

from pydantic import BaseModel


class ItemCreate(BaseModel):
    content: str
    source: str = "manual"
    status: str = "pending"


class ItemResponse(BaseModel):
    id: int
    content: str
    type: str
    source: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True