
class Book:
    '''A class representing information about a book.'''

    def __init__(self, bookTitle, bookAuthor, bookID):
        '''
        Initialize a  Book with title, author, and id.
        
        Parameters  :
        bookTitle   : The title of the book.
        bookAuthor  : The author of the book.
        bookID      : A unique identifier of the book.

        '''
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.bookID = bookID

    def setBook(self):
        '''This function is used to gather information about a book in a list.'''
        bookInfo = []
        bookInfo.append(self.bookTitle)
        bookInfo.append(self.bookAuthor)
        bookInfo.append(self.bookID)
        return
        
class Library(Book):
    '''A class representing library of book.'''

    def __init__(self):
        '''Initialize a  Library with an empty list.'''
        self.listBooks = []

    def printListBooks(self):
        '''This function is to print the information about the book(s).'''
        result = ""
        if self.listBooks == []:
            print("There's no book in this Library. Please add book first.")
        for book in self.listBooks:
            print(f"Book Title: {book.bookTitle}\nAuthor: {book.bookAuthor}\nBook ID: {book.bookID}")
            result += f"Book Title: {book.bookTitle}\nAuthor: {book.bookAuthor}\nBook ID: {book.bookID}" 
        return result
        
    
    def addNewBook(self, newBook):
        '''
        This function is to add the new book information to library.
        
        Parameters  :
        newBook     : The book object to be added to library.

        '''
        self.listBooks.append(newBook)
        return

    def removeBook(self, rbookID):
        ''''
        This function is to remove book from the library by its ID.
        
        Parameters  :
        rbookID     : The ID of the book to be removed.
        
        '''
        for book in self.listBooks:
            if book.bookID == rbookID:
                self.listBooks.remove(book)
        return

    
    def searchBook(self, sBookTitle=None, sBookAuthor=None):
        '''
        This function is to search book in the library by its ID.

        Parameters  :
        sbookID     : The ID of the book to be searched. 

        '''
        foundBook =""
        for book in self.listBooks:
            if book.bookTitle == sBookTitle:
                print(f"Book Title: {book.bookTitle}\nAuthor: {book.bookAuthor}\nBook ID: {book.bookID}\n")
                foundBook += (f"Book Title: {book.bookTitle}\nAuthor: {book.bookAuthor}\nBook ID: {book.bookID}\n")
                return foundBook
            if book.bookAuthor == sBookAuthor:
                print(f"Book Title: {book.bookTitle}\nAuthor: {book.bookAuthor}\nBook ID: {book.bookID}\n")
                foundBook += (f"Book Title: {book.bookTitle}\nAuthor: {book.bookAuthor}\nBook ID: {book.bookID}\n")
                return foundBook
        print("The book is not in  the library.")
   
    def checkLength(self):
        return len(self.listBooks)   

    def play(self):
        isPlaying = True
        while isPlaying:
            print("Menu:\n1. Add book\n2. Search book\n3. Remove book\n4. Display all book\n5. Exit")
            try:
                q1 = input("Choose menu: ")
                if q1 == "1": 
                    bookTitle = input("Input Book Title: ")
                    bookAuthor = input("Input Author: ")
                    bookID = input("Input Book ID: ")
                    newBook = Book(bookTitle, bookAuthor, bookID)
                    self.addNewBook(newBook)
                    print(f"Book with ID {newBook.bookID} has been added to library. ")
                elif q1 == "2":
                    choose = input("By title or author: ")
                    if choose == "title":
                        byTitle = input("Input book title: ")
                        self.searchBook(sBookTitle = byTitle)
                    elif choose == "author":
                        byAuthor = input("Input author name: ")
                        self.searchBook(sBookAuthor = byAuthor) 
                elif q1 == "3":
                    rmv = input("Input Book ID: ")
                    lenBefore = self.checkLength()
                    self.removeBook(rmv)
                    lenAfter = self.checkLength()
                    if lenBefore > lenAfter:
                        print(f"Book with ID {rmv} has been removed. ")
                    else:
                        print("There's no book with given ID.")
                elif q1 == "4":  
                    self.printListBooks()    
                elif q1 == "5":
                    isPlaying = False
                else:
                    print("Please try again")
            except:
                print("an error has occured")     

if __name__ == '__main__':
    library = Library()
    library.play()
