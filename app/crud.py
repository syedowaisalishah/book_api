from sqlalchemy.orm import Session
from . import sqlmodels, schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = sqlmodels.Book(**book.model_dump())  # updated for Pydantic v2
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(sqlmodels.Book).all()

def get_book(db: Session, book_id: int):
    return db.query(sqlmodels.Book).filter(sqlmodels.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = get_book(db, book_id)
    if db_book:
        for key, value in book.model_dump().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
