-- Capstone Database Setup and Import Script

-- Step 1: Create and select the main database
CREATE DATABASE IF NOT EXISTS capstone_db;
USE capstone_db;

-- Step 2: Create my table (TMDB API)
CREATE TABLE IF NOT EXISTS movies_jennifer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    release_date DATE,
    popularity FLOAT,
    overview TEXT
);

-- Step 3: Create Natalina's table
CREATE TABLE IF NOT EXISTS movies_natalina (
    movie_id VARCHAR(20) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genres TEXT,
    content_rating VARCHAR(50),
    release_date DATE,
    description TEXT
);

-- Step 4: Create Ryan's table (final structure for site)
CREATE TABLE IF NOT EXISTS movies_ryan (
    title VARCHAR(100) NOT NULL UNIQUE,
    year INT UNSIGNED NOT NULL,
    rating VARCHAR(12) NOT NULL,
    genre VARCHAR(100) NOT NULL
);

-- Optional: Copy Ryan's data from filmdata if already imported
-- (Uncomment if needed)
-- INSERT INTO movies_ryan (title, year, rating, genre)
-- SELECT Title, Year, Rating, Genre FROM filmdata;

-- Step 5: Check your tables have data
SELECT * FROM movies_jennifer;
SELECT * FROM movies_natalina;
SELECT * FROM movies_ryan;
