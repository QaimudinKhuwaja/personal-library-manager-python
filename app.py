from main import BookCollection
import frontend

if __name__ == "__main__":
    book_manager = BookCollection()
    frontend.start_gui(book_manager)