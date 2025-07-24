from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, db

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@router.post("/", response_model=schemas.Book)
def create(book: schemas.BookCreate, database: Session = Depends(get_db)):
    return crud.create_book(database, book)

@router.get("/", response_model=list[schemas.Book])
async def read_all(database: Session = Depends(get_db)):
    return crud.get_books(database)

@router.get("/{book_id}", response_model=schemas.Book)
def read(book_id: int, database: Session = Depends(get_db)):
    book = crud.get_book(database, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=schemas.Book)
def update(book_id: int, book: schemas.BookCreate, database: Session = Depends(get_db)):
    updated = crud.update_book(database, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}")
def delete(book_id: int, database: Session = Depends(get_db)):
    deleted = crud.delete_book(database, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"ok": True}
