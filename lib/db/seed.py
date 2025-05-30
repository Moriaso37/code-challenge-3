import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from lib.model.author import Author
from lib.model.magazine import Magazine
from lib.model.article import Article
from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(open("lib/db/schema.sql").read())
    conn.commit()
    conn.close()

    alice = Author(name="Alice Walker")
    alice.save()

    bob = Author(name="Bob Dylan")
    bob.save()

    toni = Author(name="Toni Morrison")
    toni.save()

    mag1 = Magazine(name="Literature Now", category="Literature")
    mag1.save()

    mag2 = Magazine(name="Music Weekly", category="Music")
    mag2.save()

    mag3 = Magazine(name="Poetry Journal", category="Poetry")
    mag3.save()

    alice.add_article(mag1, "The Color Purple")
    alice.add_article(mag3, "Everyday Use")

    bob.add_article(mag2, "Blowin' in the Wind")
    bob.add_article(mag2, "Like a Rolling Stone")
    bob.add_article(mag2, "Mr. Tambourine Man")

    toni.add_article(mag1, "Beloved")
    toni.add_article(mag3, "Recitatif")

    print("🌱 Database seeded successfully!")

if __name__ == "__main__":
    seed()
