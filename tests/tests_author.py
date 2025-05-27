import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.model.author import Author
from lib.db.connection import get_connection


@pytest.fixture(autouse=True)
def setup_and_teardown():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors")
    conn.commit()
    conn.close()
    yield

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors")
    conn.commit()
    conn.close()



def test_author_creation_and_save():
    author = Author(name="John Doe")
    author.save()
    assert author.id is not None

  
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE id = ?", (author.id,))
    row = cursor.fetchone()
    assert row['name'] == "John Doe"
    conn.close()

def test_find_author_by_id():
    author = Author(name="Jane Doe")
    author.save()
    found = Author.find_by_id(author.id)
    assert found is not None
    assert found.name == "Jane Doe"

def test_find_author_by_name():
    author = Author(name="Jane Smith")
    author.save()
    found = Author.find_by_name("Jane Smith")
    assert found is not None
    assert found.name == "Jane Smith"
