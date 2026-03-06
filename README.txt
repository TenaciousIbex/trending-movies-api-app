##Trending Movies Web Application
Flask web application that pulls trending movie data from the TMDB API, stores it in MySQL, and displays it through a dynamic web interface.

CS-10430
##Author
Jennifer Olland
Rowan University
Spring 2025 - Capstone Experience

## Project Overview

This project is a collaborative web application that pulls data from multiple movie-related APIs stores the data in a MySQL database hosted on Railway, and displays the results on a dynamic Flask-based website.

Each team member selected a unique movie API, parsed relevant data, stored it in a shared database, and built a unified user interface to display combined content.

---

## Technologies Used:
------------------
- Python 3
- Flask
- MySQL Workbench
- TMDB API (Jennifer)
- Custom SQL files from team members (Ryan & Natalina)
- HTML / Jinja2 templates

---

##Team Contributions

| Member    | API Focus                    | Table Name         |
|-----------|------------------------------|--------------------|
| Jennifer  | TMDB Trending Movies         | `movies_jennifer`  |
| Natalina  | Genre + Content Ratings      | `movies_natalina`  |
| Ryan      | Top-Rated Historical Picks   | `movies_ryan`      |

---

##Technologies Used

- Python 3.11
- Flask
- MySQL via [Railway](https://railway.app)
- TMDB API for trending movie data
- HTML + Jinja2 templating
- dotenv for environment variable security

---

##Files:

MyProjectFolder/
├── app.py # Flask backend server
├── movie_api.py # API connection + MySQL data insertion
├── templates/
│ └── index.html # HTML with Jinja2 to display movie data
├── .env # Stores API keys and DB credentials (NOT shared)
├── capstone_db_setup.sql # Creates shared MySQL schema
└── README.md # You're reading this

---

##To Run:

1. Make sure MySQL server is running and database is imported
2. Run: `python movie_api.py` to load data (Install dependencies)
3. Run: `python app.py`
4. Open your browser and go to `http://127.0.0.1:5000`

---

##Credits:
Team: Jennifer (TMDB API), Ryan (Top Picks), Natalina (Genre & Ratings)
Instructor: Professor Michael Chu
Course: CS-10430 – Capstone Experience

---

Stage 1&2

TMDB API → movie_api.py → MySQL Database
                ↓
            app.py (Flask)
                ↓
        index.html (Webpage)


movie_api.py loads data into MySQL(run when you want new data)
app.py pulls that data and serves it to the browser
index.html displays the data as a functional webpage



