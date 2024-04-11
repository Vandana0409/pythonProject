class Netflix:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def get_details(self):
        return f"Title: {self.title}\nGenre: {self.genre}\nYear: {self.year}\nRating: {self.rating}"

# Example usage:
if __name__ == "__main__":
    # Create a Netflix instance
    movie1 = Netflix("The Shawshank Redemption", "Drama", 1994, 9.3)

    # Get details of the movie
    print(movie1.get_details())
