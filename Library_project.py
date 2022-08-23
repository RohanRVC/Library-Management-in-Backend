#Createalibrary class
#display book
#lend book(who owns the book if not present)
#add book
#return book
#RVC Library
#    =Library(listofbooks,library_name)
#dictionary(books-nameofperson)
#createamain function and run an infinite while loop asking
#users for their input

# from ast import Continue

# from numpy import intp


from logging import exception
from datetime import datetime

print("Welcome to Rohan's Library")
class Library:
    books_available=["Avengers","Mirzapur","Harry Potter","Doreamon","2 Prince","The Old Man"]
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        return "done"
class LendBook(Library):
    
    def __init__(self,name="none",age=0) -> None:
        super().__init__(name,age)
    def lends():
        
        
            print("This are the Available books in our Library-:",Library.books_available)
            bookwant=input("Enter the Book u want-:")
            names=input("Enter your name-:")
            bookwants=bookwant.capitalize()
            if bookwants not in li :
                
                
                if bookwants not in li:
                    li.append(bookwants)
                
            # for i in bookwants
                dicts[bookwants]=names
                return f"{bookwants} book is now Issued to {names}."
                
            else:
                # for i in Library.books_available:

                if bookwants in li:
                    
                    return f"{bookwants} book is Issued by {dicts.get(bookwants)}.\n kindly choose another book"
            
class AddBooks(LendBook):
    def addingbooks():
        addbook=input("Add Book-:")

        addbooks=addbook.title()
        
        lib=Library.books_available
        lib.append(addbooks)
        return f" {addbooks} Book Added. Thank for donating :) "
class ReturnBook(AddBooks): 
    def returning():
        
        if li==[]:
            return f"There is no book to Return .\n Thank :)"
        else:
            print(li)
            returns=input("Which book u want to return from the list given above-:")
            ret=returns.capitalize()
            dicts.pop(ret)
            li.remove(ret)
            return f"{ret} book has been returned."
        




dicts={}
li=[]
le=[]
try:
    while True:
        print("Press 1 to display Total Books  \n Press 2 to lend Book \n Press 3 to Add Books \n Press 4 to Return Book\n Print 5 to see Lended Books\n Want to Owner Name Press 6-:")
        no=int(input())
        if no ==1:
            print(Library.books_available)
        elif no ==2:
            print(LendBook.lends())
        elif no ==3:
            # addbook=input("Add Book-:")
            # lib=Library.books_available
            # ar=lib.append(addbook)
            # print(f" {ar} Book Added. Thank for donating :) ")
            print(AddBooks.addingbooks())
        elif no ==4:
            print(ReturnBook.returning())
        # elif no ==5:
        #     print(le)
        #     pass
        elif no==5:
            if dicts=={}:
                print("No Books has been Issued to anyone Yet :)")
            else:
                print(dicts)
        elif no==6:
            print("Owner Name is Rohan Vinay Chaudhary")
        elif no==7:
            print(li)
        else:
            print("Enter Correct no please :)")
        print()
        print("Do u want to continue if yes then Press Anything \n Or press N or n to quit Program-:")
        nos=input()
        if nos=='n' or nos=='N':
            break
        else:
            continue
except:
    raise exception("Plz,Enter Numbers only")

