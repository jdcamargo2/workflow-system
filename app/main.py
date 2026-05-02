from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.core.classifier import classify_text
from app.db import Base, engine, get_db
from app.models import Item
from app.schemas import ItemCreate, ItemResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Workflow system running"}


@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    detected_type = classify_text(item.content)

    db_item = Item(
        content=item.content,
        type=detected_type,
        source=item.source,
        status=item.status,
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


@app.get("/items", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()