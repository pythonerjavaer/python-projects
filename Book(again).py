class Book:
    def __init__(self, title: str, num_pages: int, price: float):
        self.title = title
        self.num_pages = num_pages
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Book):
            return other.title == self.title and \
            other.num_pages == self.num_pages and \
            other.price == self.price
        return False
        
    def __repr__(self):
        return f"{self.title} contatins {self.num_pages} pages"

if __name__ == "__main__":
    # Part 1
    book_1 = Book("Nineteen Eighty-Four", 336, 12.00)
    book_2 = Book("Nineteen Eighty-Four", 336, 12.00)
    print(book_1 == book_2) # what does this evaluate to?

    # Part 2
    print(book_1.__eq__(book_2)) # should evaluate to True 
    print(book_1 == book_2) # should also evaluate to True

    # Part 3
    print(book_1.__repr__()) # Nineteen Eighty-Four contains 336 pages
    print(str(book_1)) # Nineteen Eighty-Four contains 336 pages
    print(book_1) # Nineteen Eighty-Four contains 336 pages