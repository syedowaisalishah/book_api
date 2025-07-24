from fastapi import FastAPI
from app.routers import books
from app import sqlmodels, db


sqlmodels.Base.metadata.create_all(bind=db.engine)

app = FastAPI(title="Book API")
app.include_router(books.router)
