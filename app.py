import requests
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def book():
    if request.method == "POST":
        genre = request.form["genre"]
        number_of_searches = request.form["number_of_searches"]
        
        # Construct the URL with the user input
        url = f'https://openlibrary.org/subjects/{genre}.json?limit={number_of_searches}'
        response = requests.get(url)
        
        if response.status_code == 200:
            books = response.json()
            
            # Check if the 'works' key exists and if it contains data
            if 'works' in books:
                # Extract titles from the 'works' list (handling the 'title' list inside each work)
                book_titles = []
                for book in books['works']:
                    # Assuming 'title' is a list in each 'work' dictionary
                    titles = book.get('title', [])
                    if isinstance(titles, list):
                        book_titles.extend(titles)  # If it's a list, extend with the titles
                    else:
                        book_titles.append(titles)  # Otherwise, just add the title
            else:
                book_titles = []
        else:
            book_titles = []
            error_message = "There was an issue retrieving the data. Please try again later."
            return render_template("index.html", error_message=error_message)

        # Return the results to the HTML page
        return render_template("index.html", genre=genre, book_titles=book_titles)

    return render_template("index.html", genre=None, book_titles=None)

