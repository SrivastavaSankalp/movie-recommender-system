#  Movie Recommender System

## Problem Statement

With the vast number of movies available today, users often struggle to decide what to watch. Most platforms either overwhelm users with choices or provide limited filtering options.

This project aims to build a simple yet effective command-line based movie recommender system that allows users to explore movies based on different criteria and discover relevant suggestions.

## Project Overview

This is a CLI-based movie recommender system built using Python and Pandas.  
It allows users to search and filter movies based on genre, rating, year, or name, and also provides similar movie recommendations.

The system is designed to be interactive, user-friendly, and efficient for exploring a curated dataset of top IMDb movies.

## Features

- Search movies by name
- Filter movies by genre
- Search by rating
  - Minimum rating
  - Exact rating range
  - Custom range
- Filter by year
  - Specific year
  - Year range
- View complete movie details
  - Title
  - Year
  - Genre
  - Runtime
  - IMDb rating
  - Plot summary
  - Director
  - Cast
- Get similar movie recommendations
- Pagination support for browsing large result sets

## Tech Stack
- Python
- Pandas

## Project Structure
TV_SHOWS_PROJECT/
│
├── src/
│ ├── main.py
│ └── imdb_top_1000.csv
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

## Requirements

Make sure you have Python installed (version 3.8 or above recommended).

Install required libraries using:

```bash
pip install -r requirements.txt

## Future Improvements

- Improve recommendation system using plot-based similarity (NLP techniques)
- Allow combining filters (genre + rating + year) for more precise results
- Add search by actor and director
- Enhance similarity logic beyond simple genre matching
- Build a web-based interface using Streamlit
- Add support for user preferences and personalized recommendations
- Improve input handling and error messages for better user experience
