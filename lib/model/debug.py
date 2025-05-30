import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import connection and models
from lib.db.connection import get_connection
from lib.model.author import Author
from lib.model.magazine import Magazine
from lib.model.article import Article

# Optional: Get the database connection to ensure it's set up
conn = get_connection()  # This will connect to the database when imported

if __name__ == "__main__":
    try:
        author = Author.find_by_id(1)
        if author:
            print(f"Author: {author}")
            print(f"Articles: {author.articles()}")
            print(f"Magazines: {author.magazines()}")
        else:
            print("No author with ID 1 found.")

        magazine = Magazine.find_by_id(1)
        if magazine:
            print(f"Magazine: {magazine}")
            print(f"Contributors: {magazine.contributors()}")
            print(f"Articles: {magazine.articles()}")
        else:
            print("No magazine with ID 1 found.")

    except Exception as e:
        print(f"An error occurred: {e}")
