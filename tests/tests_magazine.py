import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.model.magazine import Magazine
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_and_teardown():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()
    yield
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_magazine_creation_and_save():
    mag = Magazine(name="Health Times", category="Health")
    mag.save()
    assert mag.id is not None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines WHERE id = ?", (mag.id,))
    row = cursor.fetchone()
    assert row['name'] == "Health Times"
    assert row['category'] == "Health"
    conn.close()

def test_find_magazine_by_id():
    mag = Magazine(name="Nature World", category="Nature")
    mag.save()
    found = Magazine.find_by_id(mag.id)
    assert found is not None
    assert found.name == "Nature World"

def test_find_magazine_by_name():
    mag = Magazine(name="History Monthly", category="History")
    mag.save()
    found = Magazine.find_by_name("History Monthly")
    assert found is not None
    assert found.name == "History Monthly"
