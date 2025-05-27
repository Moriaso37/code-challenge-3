import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.model.article import Article
from lib.model.author import Author
from lib.model.magazine import Magazine
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_and_teardown():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()
    yield
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_article_creation_and_save():
    author = Author(name="Author A")
    author.save()
    magazine = Magazine(name="Tech World", category="Technology")
    magazine.save()

    article = Article(title="Future of AI", author_id=author.id, magazine_id=magazine.id)
    article.save()

    assert article.id is not None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE id = ?", (article.id,))
    row = cursor.fetchone()
    assert row['title'] == "Future of AI"
    conn.close()

def test_find_article_by_id():
    author = Author(name="Author B")
    author.save()
    magazine = Magazine(name="Science Weekly", category="Science")
    magazine.save()
    article = Article(title="Quantum Computing", author_id=author.id, magazine_id=magazine.id)
    article.save()

    found = Article.find_by_id(article.id)
    assert found is not None
    assert found.title == "Quantum Computing"
