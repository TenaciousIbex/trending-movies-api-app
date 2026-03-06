'''This script handles data collection and storage.
It connects to the TMDB API using the API key stored in an .env file.
Parses selected movie info (title, release date, popularity, overview),
and saves it into the hosted Railway MySQL database for use in the site.
'''
# Imports
import os
from dotenv import load_dotenv
import requests
import json
import mysql.connector

#tell Python where to find the .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

#debug print to confirm .env loaded
print("Loaded DB_PORT:", os.getenv("DB_PORT"))  # should show 46672
print("API_KEY:", os.getenv("API_KEY"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_NAME:", os.getenv("DB_NAME"))

# API Key and Endpoint
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.themoviedb.org/3/trending/movie/day"

GENRE_MAP = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Sci-Fi",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}


# Railway MySQL DB Config
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_trending_movies():
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": 1
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        movies = response.json()
        extracted_movies = []

        for movie in movies.get("results", []):
             genre_ids = movie.get("genre_ids", [])
             genres = ", ".join([GENRE_MAP.get(gid, "Unknown") for gid in genre_ids])
             poster_path = movie.get("poster_path")
             poster_url = f"https://image.tmdb.org/t/p/w200{poster_path}" if poster_path else ""
             extracted_movies.append({
                "title": movie.get("title"),
                "release_date": movie.get("release_date"),
                "popularity": movie.get("popularity"),
                "overview": movie.get("overview"),
                "poster_url": poster_url,
                "genres": genres #use mapped genres now
            })

        return extracted_movies
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

def save_to_mysql(movies):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    for movie in movies:
        try:
            #save to my table
            cursor.execute("""
                INSERT INTO movies_jennifer (title, release_date, popularity, overview, poster_url, genres)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                movie["title"],
                movie["release_date"],
                movie["popularity"],
                movie["overview"],
                movie["poster_url"],
                movie["genres"]
            ))
            
			#save to natalina's table
            cursor.execute("""INSERT IGNORE INTO movies_natalina (movie_id, title, genres, content_rating, release_date, description)
                           VALUES (%s, %s, %s, %s, %s, %s)
                           """, (
                               movie["title"].lower().replace(" ", "_"), #basic unique id
                               movie["title"],
                               "Drama",#placeholder genre
                               "PG-13", #placeholder rating
                               movie["release_date"],
                               movie["overview"]
						   ))
        except Exception as e:
            print("Insert error:", e)

    connection.commit()
    cursor.close()
    connection.close()
    print("Movies saved to MySQL!(Jennifer & Natalina)")
    print(json.dumps(movies, indent=4))

if __name__ == "__main__":
    trending = get_trending_movies()
    if trending:
        print(json.dumps(trending, indent=4))
        save_to_mysql(trending)
