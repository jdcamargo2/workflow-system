from sqlalchemy import Column, DateTime, Integer, String, Text, func

from app.db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    type = Column(String(50), nullable=False, default="note")
    source = Column(String(50), nullable=False, default="manual")
    status = Column(String(50), nullable=False, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)