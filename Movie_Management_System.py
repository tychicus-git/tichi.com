#Project: Movie_manager
#Author: Tychicus Mbeja
#Date: Friday 6th June 2025
#Description: Movie_manager is a program that allows users to handle their movie lists. It allows the user to add as many movies as they can and their
#             details so thsat they can keep track of their movies. The user can add movies into their lists,view them, update them, delete them and 
#             even search them. 
#Class movie that has attributes of each movie that is added
class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
#This function allows the program to print the output whenever print () is used
    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Year: {self.year}"

#Class moviemanager has functions /methods that are used to carry out the different tasks 
class MovieManager:   
    def __init__(self):
#This is the empty list in which movies will be stored
        self.movies = []
#This function prompts the user for their name and and welcomes them to the program   
    def greeting(self):
        username = input ("\nWelcome, please input your name: ")
        print(f"\nDear {username}, Welcome to your Movie List Management System")
    
#This funtion displays the tasks the program offers
    def display_menu(self):
        print("\nPick an option to proceed")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Search Movie")
        print("6. Exit")
#This is the function that manages adding movies into the program
    def add_movie(self):
#Here the user is prompted to input details of their movie of prefernce 
        title = input("Enter Movie Title: ").strip()
        genre = input("Enter Genre: ").strip()
        year = input("Enter Release Year: ").strip()
#The details are called in the object  (new_movie) and stored in the list (self.movies)
        new_movie = Movie(title, genre, year)
        self.movies.append(new_movie)
        print("\nYour movie has been successfully added!")
#This function runs the task to view the movies in the list (self.movies). If no movies are found it prints no movies found 
    def view_movies(self):
        if not self.movies:
            print("No movies found.")
            return
        print("\nMovies List:")
#for any movies in the list they are listed in order starting from one
        for i, movie in enumerate(self.movies, 1):
            print(f"{i}. {movie}")
#This function runs the task of updating movies. It asks for the movie title to update from the user
    def update_movie(self):
        title = input("Enter the title of the movie to update: ").strip()
#If the title given matches with the one in the list, the user can now update any information of the movie 
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                new_title = input("Enter new title (leave blank to keep current): ").strip()
                new_genre = input("Enter new genre (leave blank to keep current): ").strip()
                new_year = input("Enter new release year (leave blank to keep current): ").strip()
#The new information is updated
                movie.title = new_title or movie.title
                movie.genre = new_genre or movie.genre
                movie.year = new_year or movie.year
                print("\nMovie been successfully updated!")
                return
        print("Movie not found.")
#This function runs the task of deleting movies from the list. It prompts for the title of the movie to be deleted
    def delete_movie(self):
        title = input("Enter Movie Title to Delete: ").strip()
#If the title of the movie matches the one in the list, it prompts for confirmation before deleting the given movie
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                confirm = input(f'Are you sure you want to delete "{title}"? (yes/no): ').strip().lower()
                if confirm == "yes":
                    self.movies.remove(movie)
                    print("Movie has been successfully deleted!")
                else:
                    print("Delete Cancelled.")
                return
        print("Movie not found.")
#This function runs the task of searching for movies in the program. It prompts for the title of the movie being searched
    def search_movie(self):
        title = input("Enter Movie Title to Search: ").strip()
#If the title matches the ones in the list it prints out movie found if not then it prints out movie not found 
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                print(f"Found: {movie}")
                return
        print("Movie not found.")
#This funtion allocates the different functions to their respective choices. It makes it easier to run the whole code by just calling one method
    def run(self):
        self.greeting()
        while True:
            self.display_menu()
            choice = input("\nEnter choice: ").strip()
            if choice == "1":
                self.add_movie()
            elif choice == "2":
                self.view_movies()
            elif choice == "3":
                self.update_movie()
            elif choice == "4":
                self.delete_movie()
            elif choice == "5":
                self.search_movie()
            elif choice == "6":
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

#This if statement checks whether the program is running directly and is not being imported.It therefore runs the program as the main source 
# it then creates an object (manager) for the class (MovieManager) and uses it to call the method (.run()) which runs the whole code. 
if __name__ == "__main__":
    manager = MovieManager()
    manager.run()
