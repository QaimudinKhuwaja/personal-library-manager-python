from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

def start_gui(book_manager):
    root = Tk()
    root.geometry("1000x600")
    root.title("Personal Library Manager")

    title_label = Label(root, text="Book Title")
    author_label = Label(root, text="Author")
    year_label = Label(root, text="Publication Year")
    genre_label = Label(root, text="Genre")
    is_read = ttk.Combobox(root, values=["Yes", "No"])
    is_read.set("Have you Read?")

    title_entry = Entry(root)
    author_entry = Entry(root)
    year_entry = Entry(root)
    genre_entry = Entry(root)

    table = ttk.Treeview(root, columns=("Book No","Title", "Author", "Year", "Genre", "Status"), show="headings")
    table.column("Book No", width=80)
    table.column("Title", width=100)
    table.column("Author", width=100)   
    table.column("Year", width=100)
    table.column("Genre", width=100)
    table.column("Status", width=100)
    table.heading("Book No", text="Book No")
    table.heading("Title", text="Title")
    table.heading("Author", text="Author")
    table.heading("Year", text="Year")
    table.heading("Genre", text="Genre")
    table.heading("Status", text="Status")


    table.grid(row=2, column=2, rowspan=6, padx=10, pady=10)
    title_label.grid(row=0, column=0, padx=10, pady=10)
    author_label.grid(row=1, column=0, padx=10, pady=10)
    year_label.grid(row=2, column=0, padx=10, pady=10)
    genre_label.grid(row=3, column=0, padx=10, pady=10)

    is_read.grid(row=4, column=1, padx=10, pady=10)
    title_entry.grid(row=0, column=1, padx=10, pady=10)
    author_entry.grid(row=1, column=1, padx=10, pady=10)
    year_entry.grid(row=2, column=1, padx=10, pady=10)
    genre_entry.grid(row=3, column=1, padx=10, pady=10)
    search_enrty = Entry(root)
    search_enrty.grid(row=1, column=2, padx=10, pady=10)

    def add_book():
       book_manager.create_new_book(
            title_entry.get(),
            author_entry.get(),
            year_entry.get(),
            genre_entry.get(),
            is_read.get()
        )

    def delete_book():
        is_deleted = book_manager.delete_book(title_entry.get())
        if is_deleted:
            return messagebox.showinfo("Book Deleted", "Book deleted successfully!")
        return messagebox.showerror("Error", "Book not found in the collection.")

    def view_books():
        for i in table.get_children():
            table.delete(i)
        books = book_manager.show_all_books()
        for book in books:
            table.insert("", "end", values=(book))

    def search_books():
        if search_enrty.get() == '':
            return messagebox.showerror("Error", "Please Enter Book or Author name.")
        searched_books = book_manager.find_book(search_enrty.get())
        if searched_books:
            for i in table.get_children():
                table.delete(i)
            for book in searched_books:
                table.insert("", "end", values=(book))
        else:
            return messagebox.showerror("Error", "No book found.")
        
    def reading_progress():
        total_books, completion_rate = book_manager.show_reading_progress()
        messagebox.showinfo("Reading Progress", f"Total Books: {total_books}\nReading Progress: {completion_rate}")
        
    add_button = Button(root, text="Add Book", command=add_book)
    add_button.grid(row=5, column=1, padx=10, pady=10)

    delete_button = Button(root, text="Delete Book", command=delete_book)
    delete_button.grid(row=5, column=0, padx=10, pady=10)

    view_button = Button(root, text="View Books", command=view_books)
    view_button.grid(row=6, column=1, padx=10, pady=10)

    search_button = Button(root, text="Search", command=search_books)
    search_button.grid(row=1, column=3, padx=10, pady=10)

    reading_progress_button = Button(root, text="Reading Progress", padx=10, pady=10, command=reading_progress)
    reading_progress_button.grid(row=6, column=0, padx=10, pady=10)
    
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

    