import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from lib.db.connection import get_connection
from lib.model.author import Author
from lib.model.magazine import Magazine
from lib.model.article import Article


conn = get_connection()  

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
