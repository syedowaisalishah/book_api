from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., gt=0, lt=2100)
    summary: Optional[str] = None

class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True
