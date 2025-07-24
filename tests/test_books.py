from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book():
    res = client.post("/books/", json={
        "title": "Book A",
        "author": "Author A",
        "published_year": 2023,
        "summary": "A great book"
    })
    assert res.status_code == 200
    assert res.json()["title"] == "Book A"
    return res.json()["id"]

def test_read_book():
    book_id = test_create_book()
    res = client.get(f"/books/{book_id}")
    assert res.status_code == 200
    assert res.json()["id"] == book_id

def test_read_all_books():
    res = client.get("/books/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_update_book():
    book_id = test_create_book()
    res = client.put(f"/books/{book_id}", json={
        "title": "Book Updated",
        "author": "Author Updated",
        "published_year": 2024,
        "summary": "Updated summary"
    })
    assert res.status_code == 200
    assert res.json()["title"] == "Book Updated"

def test_delete_book():
    book_id = test_create_book()
    res = client.delete(f"/books/{book_id}")
    assert res.status_code == 200
    assert res.json()["ok"] is True
