import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from lib.db.connection import get_connection

from lib.model.author import Author
from lib.model.magazine import Magazine
from lib.model.article import Article

if __name__ == "__main__":
    author = Author.find_by_id(1)
    print(author)
    print(author.articles())
    print(author.magazines())

    magazine = Magazine.find_by_id(1)
    print(magazine)
    print(magazine.contributors())
    print(magazine.articles())
