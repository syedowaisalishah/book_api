from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Utility to create a book and return its ID
def create_sample_book():
    res = client.post("/books/", json={
        "title": "Sample Book",
        "author": "Sample Author",
        "published_year": 2023,
        "summary": "Sample Summary"
    })
    assert res.status_code == 201
    return res.json()["id"]

# Create Book
def test_create_book():
    res = client.post("/books/", json={
        "title": "Book A",
        "author": "Author A",
        "published_year": 2023,
        "summary": "A great book"
    })
    assert res.status_code == 201
    assert res.json()["title"] == "Book A"

# Read Book by ID
def test_read_book():
    book_id = create_sample_book()
    res = client.get(f"/books/{book_id}")
    assert res.status_code == 200
    assert res.json()["id"] == book_id

# Read All Books
def test_read_all_books():
    res = client.get("/books/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

# Update Book
def test_update_book():
    book_id = create_sample_book()
    updated_data = {
        "title": "Book Updated",
        "author": "Author Updated",
        "published_year": 2024,
        "summary": "Updated summary"
    }
    res = client.put(f"/books/{book_id}", json=updated_data)
    assert res.status_code == 200
    assert res.json()["title"] == "Book Updated"

# Delete Book
def test_delete_book():
    book_id = create_sample_book()
    res = client.delete(f"/books/{book_id}")
    assert res.status_code == 204  # No content

    # Confirm deletion
    res = client.get(f"/books/{book_id}")
    assert res.status_code == 404

# Invalid Book ID
def test_get_book_invalid_id():
    res = client.get("/books/99999")
    assert res.status_code == 404

# Delete Already Deleted
def test_delete_already_deleted():
    book_id = create_sample_book()
    client.delete(f"/books/{book_id}")
    res = client.delete(f"/books/{book_id}")
    assert res.status_code == 404

# Validation: Published Year Unrealistic
def test_create_book_invalid_year():
    book_data = {
        "title": "Future Book",
        "author": "Time Lord",
        "published_year": 4000,
        "summary": "Sci-fi"
    }
    response = client.post("/books/", json=book_data)
    assert response.status_code == 422
