import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self, title, author, year, genre, read):
        """Add a new book to the collection by gathering information from the user."""
        from tkinter import messagebox
        if title == "" or author == "" or year == "" or genre == "":
            return messagebox.showerror("Error", "Please fill all the fields.")
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read.strip().lower() == "yes",
        }

        self.book_list.append(new_book)
        self.save_to_file()
        return messagebox.showinfo("Book Added", "Book added successfully!")

    def delete_book(self, book_title):
        """Remove a book from the collection using its title."""

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return True
        return False

    def find_book(self, search_text):
        """Search for books in the collection by title or author name."""
        # search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        # search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text.lower() in book["title"].lower()
            or search_text.lower() in book["author"].lower()
        ]

        book_list = []
        for index, book in enumerate(found_books, 1):
            reading_status = "Read" if book["read"] else "Unread"
            book_list.append([index, book['title'], book['author'], book['year'], book['genre'], reading_status])
        return book_list
    

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.book_list:
            print("Your collection is empty.\n")
            return

        book_list = []
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            book_list.append([index, book['title'], book['author'], book['year'], book['genre'], reading_status])
        return book_list

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        return total_books, completion_rate

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.load_from_file()
    book_manager.main_menu()
    book_manager.save_to_file()
