import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lib.db.connection import get_connection

def run_example_queries():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    print("Authors:")
    for author in authors:
        print(dict(author))


    cursor.execute("SELECT * FROM magazines")
    magazines = cursor.fetchall()
    print("\nMagazines:")
    for mag in magazines:
        print(dict(mag))

    cursor.execute("""
        SELECT m.name, COUNT(a.id) as article_count
        FROM magazines m
        LEFT JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
    """)
    counts = cursor.fetchall()
    print("\nArticles per Magazine:")
    for row in counts:
        print(f"{row['name']}: {row['article_count']}")

    conn.close()

if __name__ == "__main__":
    run_example_queries()
