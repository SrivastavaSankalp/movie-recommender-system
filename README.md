#  Movie Recommender System

A command-line based movie recommender system built using Python and Pandas.

## Features
- Search movies by genre
- Search movies by rating (minimum, exact, range)
- Search movies by year (specific or range)
- Search movie by name
- View complete movie details (plot, cast, director)
- Get similar movie recommendations


## Dataset
IMDb Top 1000 Movies Dataset (1920–2020)

## Tech Stack
- Python
- Pandas

## How to Run

```bash
pip install -r requirements.txt
python src/main.py

## Future Improvements

- Implement content-based recommendation using plot similarity (NLP)
- Add multi-filter search (combine genre, rating, and year)
- Improve similarity logic beyond genre matching
- Build a web interface using Streamlit for better user experience
- Add support for user preferences and watch history