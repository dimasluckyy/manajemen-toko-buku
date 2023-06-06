class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Bookstore:", self.name)
        print("buku yang tersedia:")
        for book in self.books:
            print("--------------------")
            print("judul:", book.title)
            print("penulis:", book.author)
            print("harga:", book.price)
            print("--------------------")


def main():
    # Membuat objek Bookstore
    bookstore = Bookstore("My Bookstore")

    while True:
        print("\nOptions:")
        print("1. tambah buku")
        print("2. tampilkan daftar buku")
        print("3. Exit")

        choice = input("pilih menu di atas: ")

        if choice == "1":
            print("\nmasukkan detail buku:")
            title = input("judul: ")
            author = input("penulis: ")
            price = float(input("harga: "))

            book = Book(title, author, price)
            bookstore.add_book(book)
            print("buku berhasil di tambahkan!")

        elif choice == "2":
            bookstore.display_books()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
