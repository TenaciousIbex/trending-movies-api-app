'''
This acts as the actual server for my website.
It starts a local web server, connects to the shared Railway MySQL DB,
pulls data from each teammate's table, and renders it on the site using Flask.
'''

from flask import Flask, render_template
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
print("Loaded ENV values:")
print("Loaded DB_PORT:", os.getenv("DB_PORT"))  # should show 46672
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_USER:", os.getenv("DB_USER"))
rapidapi_key = os.getenv("RAPIDAPI_KEY")
rapidapi_host = os.getenv("RAPIDAPI_HOST")

# Database connection config from .env
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

app = Flask(__name__)

@app.route('/')
def home():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)

    #Jen's data from TMDB via movie_api.py
    cursor.execute("SELECT * FROM movies_jennifer LIMIT 10")
    jen_data = cursor.fetchall()
    
    #Natalina's Data (using RapidAPI) JOINED with Ryan's Titles
    cursor.execute("""SELECT r.title, r.year, n.description
                   FROM movies_ryan r
                   Join movies_natalina n ON r.title = n.title LIMIT 10
                   """)
    natalina_data = cursor.fetchall()

    # Ryan's data (no collaboration provided)
    cursor.execute("SELECT * FROM movies_ryan LIMIT 10")
    ryan_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", jen_data=jen_data, natalina_data=natalina_data, ryan_data=ryan_data)

@app.route('/filter/<genre>')
def filter_all_by_genre(genre):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)

    # Skip Ryan's movies since his table has no genres column
    jen_query = "SELECT * FROM movies_jennifer WHERE genres LIKE %s"
    natalina_query = "SELECT * FROM movies_natalina WHERE genres LIKE %s"

    cursor.execute(jen_query, (f"%{genre}%",))
    jen_movies = cursor.fetchall()

    ryan_movies = []  # Don't run the query, leave empty list

    cursor.execute(natalina_query, (f"%{genre}%",))
    natalina_movies = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("filtered.html", genre=genre, jen=jen_movies, ryan=ryan_movies, natalina=natalina_movies)



if __name__ == '__main__':
    app.run(debug=True)
