import requests
from flask import Flask 


genre = input('What genre would you like to search for? ')
number_of_searches = str(input('How many results would you like to display? '))
url = 'https://openlibrary.org/subjects/'+genre+'.json?limit='+number_of_searches+''
response = requests.get(url)
books = response.json()

def find_books():
    for book in books['works']:
        print(book['title'])


# app = Flask(__name__)
# @app.route("/")
# def hello():
#     genre = input('What genre would you like to search for? ')
#     number_of_searches = str(input('How many results would you like to display? '))
#     url = 'https://openlibrary.org/subjects/'+genre+'.json?limit='+number_of_searches+''
#     response = requests.get(url)
#     books = response.json()

    
#     for book in books['works']:
#         print(book['title'])