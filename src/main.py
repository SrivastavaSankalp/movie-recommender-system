import pandas as pd
import random #to genrate random number for movie 
import os

#Collects data from the given dataset
def load_data(): 
    try:
        current_dir = os.path.dirname(__file__) 
        file_path = os.path.join(current_dir, "imdb_top_1000.csv")

        df = pd.read_csv(file_path)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        df["released_year"] = pd.to_numeric(df["released_year"], errors="coerce")

        return df

    except Exception as e:
        print("❌ Error loading dataset:", e)
        return None

#function for sort by rating
def get_verdict(rating):
    try:
        rating = float(rating)
    except:
        return "N/A"

    if rating >= 8.5:
        return " A MUST WATCH "
    elif rating >= 7.5:
        return " GO FOR IT"
    elif rating >= 6.5:
        return " DECENT ONE TIME WATCH"
    else:
        return " TIMEPASS"

#shows movie information
def display_movie(row):
    cast = ", ".join(filter(None, [
        str(row.get("star1", "")),
        str(row.get("star2", "")),
        str(row.get("star3", "")),
        str(row.get("star4", ""))
    ]))

    print("\n" + "=" * 70)
    print(f"🎬 Name           : {row.get('series_title', 'N/A')}")
    print(f"📅 Released Year  : {row.get('released_year', 'N/A')}")
    print(f"🎭 Genre          : {row.get('genre', 'N/A')}")
    print(f"🔞 Certificate    : {row.get('certificate', 'N/A')}")
    print(f"⏱ Runtime        : {row.get('runtime', 'N/A')}")
    print(f"⭐ IMDb Rating    : {row.get('imdb_rating', 'N/A')}")
    print(f"🏆 Verdict        : {get_verdict(row.get('imdb_rating'))}")
    print(f"\n📝 Plot          : {row.get('overview', 'N/A')}")
    print(f"\n🎬 Director      : {row.get('director', 'N/A')}")
    print(f"👥 Cast          : {cast}")
    print("=" * 70 + "\n")

#function to browse the movies
def browse_results(results):
    page_size = 10
    total = len(results)
    index = 0

    while index < total:
        chunk = results.iloc[index:index + page_size]

        print(f"\n Showing {index + 1} to {min(index + page_size, total)} of {total}:\n")

        for i, (_, row) in enumerate(chunk.iterrows(), 1):
            print(f"{i}. {row['series_title']}  {row['imdb_rating']}")

        choice = input("\n Enter number | 'm' for more | Enter to exit: ").strip().lower()

        if choice == "m":
            index += page_size

        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(chunk):
                display_movie(chunk.iloc[idx])
                show_similar_movies(results, chunk.iloc[idx])
            else:
                print(" Invalid selection")

        else:
            break

#function to search movie based on genre
def search_by_genre(df):
    genre = input("\nEnter genre: ").strip().lower()
    results = df[df["genre"].str.lower().str.contains(genre, na=False)]

    if results.empty:
        print("❌ No results found.")
        return

    results = results.sort_values(by="imdb_rating", ascending=False)
    browse_results(results)

#funcion to search for movie based on rating
def search_by_rating(df):
    print("\n Choose how you want to search:\n")
    print("1. Minimum rating\n2. Exact rating\n3. Custom range")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        r = float(input("Enter minimum rating: "))
        results = df[df["imdb_rating"] >= r]

    elif choice == "2":
        r = float(input("Enter rating: "))
        results = df[(df["imdb_rating"] >= r) & (df["imdb_rating"] < r + 0.5)]

    elif choice == "3":
        user_input = input("Enter range (e.g., 6 to 8): ").lower()
        user_input = user_input.replace("to", " ").replace("-", " ")
        low, high = map(float, user_input.split())
        results = df[(df["imdb_rating"] >= low) & (df["imdb_rating"] <= high)]

    else:
        print("Invalid choice")
        return

    if results.empty:
        print(" No results found.")
        return

    results = results.sort_values(by="imdb_rating", ascending=False)
    browse_results(results)

#function to search movies based on year
def search_by_year(df):
    print("\nNOTE: Dataset contains movies from 1920 to 2020\n")

    choice = input("1. Specific year\n2. Range\n👉 Choice: ").strip()

    if choice == "1":
        year = int(input("Enter year: "))
        results = df[df["released_year"] == year]

    elif choice == "2":
        start = int(input("Start year: "))
        end = int(input("End year: "))
        results = df[(df["released_year"] >= start) & (df["released_year"] <= end)]

    else:
        print("Invalid choice")
        return

    if results.empty:
        print("No results found.")
        return

    results = results.sort_values(by="imdb_rating", ascending=False)
    browse_results(results)

#function for random recommendation of movies
def random_recommendations(df):
    sample = df.sample(5)

    for _, row in sample.iterrows():
        display_movie(row)


# function to show similar movies based on current movie
def show_similar_movies(df, current_movie):
    genre = current_movie.get("genre", "")
    genres = genre.split(",")

    results = df[
        df["genre"].apply(
            lambda g: any(x.strip() in g for x in genres) if isinstance(g, str) else False
        )
    ]

    results = results[results["series_title"] != current_movie["series_title"]]
    results = results.sort_values(by="imdb_rating", ascending=False).head(5)

    if results.empty:
        return

    print("\n Similar Movies:\n")

    for i, (_, row) in enumerate(results.iterrows(), 1):
        print(f"{i}. {row['series_title']}  {row['imdb_rating']}")

    choice = input("\n Select a movie (Enter to skip): ").strip()

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(results):
            display_movie(results.iloc[idx])
            show_similar_movies(df, results.iloc[idx])


# function to search movie based on name
def search_by_name(df):
    name = input("\n Enter movie name: ").strip().lower()
    results = df[df["series_title"].str.lower().str.contains(name, na=False)]

    if results.empty:
        print(" Movie not found.")
        return

    results = results.sort_values(by="imdb_rating", ascending=False)

    for i, (_, row) in enumerate(results.head(10).iterrows(), 1):
        print(f"{i}. {row['series_title']} ⭐ {row['imdb_rating']}")

    choice = input("\n Select a movie: ").strip()

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(results.head(10)):
            selected = results.iloc[idx]
            display_movie(selected)
            show_similar_movies(df, selected)

#function to show menu for movie recommendation selection
def show_menu():
    print("\n" + "=" * 70)
    print(" MOVIE RECOMMENDER SYSTEM".center(70))
    print("=" * 70)

    print("\n1. Search by Genre")
    print("2. Random Recommendations")
    print("3. Search by Rating")
    print("4. Search by Year")
    print("5. Search by Name 🔍")
    print("6. Exit\n")

#main function
def main():
    df = load_data()

    while True:
        show_menu()
        choice = input(" Enter choice: ")

        if choice == "1":
            search_by_genre(df)
        elif choice == "2":
            random_recommendations(df)
        elif choice == "3":
            search_by_rating(df)
        elif choice == "4":
            search_by_year(df)
        elif choice == "5":
            search_by_name(df)
        elif choice == "6":
            break
        else:
            print(" Invalid choice")


if __name__ == "__main__":
    main()