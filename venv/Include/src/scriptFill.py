import json, urllib.request, requests
import psycopg2
from psycopg2.extras import execute_values

def loadCategoriesToPostgress(response):
    # url = "https://www.googleapis.com/books/v1/volumes?q=isbn%3"+isbn
    # response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    # db connection
    try:
        conn = psycopg2.connect("dbname='scriptbook' user='postgres' host='localhost' password='qwerty'")
    except:
        print("I am unable to connect to the database")

    # cursor
    cur = conn.cursor()
    cont=0
    for item in data:
        cont+=1
        insert_subjects = "INSERT INTO category VALUES ({}, {})".format(cont, item['name'])
        cur.execute(insert_subjects)
        conn.commit()

    # close the cursor and connection
    cur.close()
    conn.close()

def loadAuthorsToPostgress(response):
    # url = "https://www.googleapis.com/books/v1/volumes?q=isbn%3"+isbn
    # response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    # db connection
    try:
        conn = psycopg2.connect("dbname='scriptbook' user='postgres' host='localhost' password='qwerty'")
    except:
        print("I am unable to connect to the database")

    # cursor
    cur = conn.cursor()
    cont=0
    for item in data:
        cont+=1
        insert_subjects = "INSERT INTO author VALUES ({}, {})".format(cont, item['name'])
        cur.execute(insert_subjects)
        conn.commit()

    # close the cursor and connection
    cur.close()
    conn.close()


# Retrieve Json Data from API
def loadBooksToPostgress(response):
    # url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn
    # response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    # db connection
    try:
        conn = psycopg2.connect("dbname='scriptbook' user='postgres' host='localhost' password='qwerty'")
    except:
        print("I am unable to connect to the database")

    # cursor
    cur = conn.cursor()
    bookFields = [
        'id', #varchar
        'amount', #integer
        'asset_number',  # varchar
        'abstract',  # varchar
        'edition',
        'editorial',
        'img',  # varchar
        'isbn',  # varchar
        'location',# varchar
        'registration_date', #integer
        'release_year', #integer
        'title', #varchar
    ]

    for item in data:
        my_book = [item[field] for field in bookFields]
        insert_books = "INSERT INTO book VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert_books, tuple(my_book))
        conn.commit()


    # close the cursor and connection
    cur.close()
    conn.close()

if __name__ == '__main__':
    with open('example.json', 'r') as myBooks:
        loadBooksToPostgress(myBooks)
        print("I'm a car!")

    # with open('example.json', 'r') as myCategories:
    #     loadCategoriesToPostgress()
    #     print("I'm a Bus!")
    #
    # with open('example.json', 'r') as myAuthors:
    #     loadAuthorsToPostgress(myfile)
    #     print("I'm a God!")