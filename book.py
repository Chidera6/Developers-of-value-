class Library:

    def __init__(self):
        self.shelf = {}

    def add_books(self,book_name,book_rating):
        if book_name not in self.shelf.keys():
            new_dict = {}
            new_dict[book_name] = book_rating
            self.shelf.update({book_name:new_dict})
            return self.shelf    
        return f'{book_name} already exists'

    def change_book_rating(self,book_name,book_rating):
        if book_name in self.shelf.keys():
            self.shelf[book_name] = book_rating
            return self.shelf 
        return f'{book_name} does not exist'   
         
    def get_all_books(self):
            return self.shelf

    def delete_book(self,book_name):
        if book_name in self.shelf.keys():
           del self.shelf[book_name]
           return self.shelf
        return f'{book_name} not found'
    
    def get_book_by_book_name(self,book_name):
        for book in self.shelf:
            if book == book_name:
               return self.shelf[book] 
        return f'{book_name} does not exist'
    """
    def get_book_with_same_ratings(self,book_ratings):
        for ratings in self.shelf.values():
            for x in ratings.values():
                if x == book_ratings:
                  return self.shelf[book_ratings]
            return f'{book_ratings} does not exist'
    """
    def get_book_with_same_ratings(self, book_ratings):
        books = self.shelf.values()
        book_same_rating = {}
        for book in books:
            if book_ratings in book.values() :
                book_same_rating.update(book)
        return f'No book has the rating of {book_ratings}'
        # if book_same_rating == {} else print(book_same_rating)
    



library = Library()
library.add_books("maria",5)
library.add_books("sidney sheldon",5)
print(library.get_book_with_same_ratings(5))
print(library.get_all_books())
print(library.delete_book("sidney sheldon"))
print(library.get_book_by_book_name("maria"))
print(library.get_all_books())


