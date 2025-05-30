import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open("lib/db/schema.sql", "r") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("✅ Database schema created successfully.")

if __name__ == "__main__":
    setup_db()
