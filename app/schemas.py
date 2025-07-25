from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., gt=0, lt=2100)
    summary: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class Book(BookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
