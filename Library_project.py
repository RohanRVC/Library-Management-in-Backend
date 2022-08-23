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


#####################################################################################################
# from datetime import datetime
# class Library:
#     def __init__(self,libraryname,booklist):
#         self.bookdata={}
#         self.libarayname=libraryname
#         self.booklist= booklist
#         for book in booklist:
#             self.bookdata[book] = None
#     def listofbook(self):
#         listt=self.booklist
#         print("List of the books".upper())
#         for index, books in enumerate (listt, start=1):
#             print(f"{index}: {books}")
#     def addbook(self):
#         print("Enter the book name below. You can add only one book at a time.")
#         while(True):
#             userinput=input("Name: ")
#             self.booklist.append(userinput)
#             self.bookdata[userinput]=None
#             print(f"Thank you for your contribution to the library. Your book: '{userinput}' has been successfully added to "
#                   f"our library."
#                   )
#             print("Do you want to add another book?")
#             userinfo=int(input("1: yes, 2:No"))
#             if userinfo==1:
#                 continue
#             else:
#                 print("See you soon...")
#                 break
#     def lendbook(self):
#         print("Which book you are looking for ???")
#         userlend=input("Book name:").capitalize()
#         if userlend in self.booklist:
#             print("Checking the availability of the book...\n")
#             if self.bookdata[userlend] is None:
#                 print(f"The book '{userlend}', you requested is currently available.\n")
#                 print("Do you want to lend it: ")
#                 lendingpermission = int(input("1.yes 2.No"))
#                 if lendingpermission == 1:
#                     username = input("To lend a book you have to provide your name.\nYour name:")
#                     self.bookdata[userlend]=username
#                     with open("lendrecord.txt","a") as lr:
#                         presentdate=datetime.now()
#                         lr.write(f"Date:{[str(presentdate)]}, Book_name:{userlend}, Username:{username}\n")
#                     print("Your name has been registered successfully\n")
#                     print("List of the book with the name of student who took the book".upper())
#                     # for key, val in self.bookdata.items() :
#                     #     if val!=None:
#                     #         print(f"Book: {key} -- Student's name: {val}")
#             else:
#                 print(f"This book has already been taken by {self.bookdata.get(userlend)}.\nIt will be available in thisthis date...\nReserver for me (option)")
#         else:
#             print(f"Sorry there is no book named as '{userlend}' in our library. Please type the spelling of the book correctly.")

#     def returnbook(self):
#         print("Enter your username")
#         username=input("Username:")
#         for key,value in self.bookdata.items():
#             if value!=None:
#                 if value == username:
#                     print(key, value)
#                     print(f"You borrowed {key} book on this this date")
#                     self.bookdata[key]=None
#                     with open("bookreturnrecord.txt","a") as brr:
#                         returndate=datetime.now()
#                         brr.write(f"Date:{[str(returndate)]}, Book_name:{key}, Username:{username}\n")
#                     # self.bookdata.pop(key)
#                     print("The book has been released.")
#                     break
#                 else:
#                     print(f"The username is incorrect.\nUser name {username} has not been registered yet.")
#     def bookdel(self):
#         print("Now you have access to delete the book from the library.")
#         admindel=input("Which book you want to delete? ").capitalize()
#         print(self.booklist)
#         self.booklist.remove(admindel)
#         print(self.booklist)

# def main():
#     listofbooks=["Math", "Science","Nepali"]
#     libraryname="RVC's library"
#     shreelibrary=Library(libraryname, listofbooks)
#     adminpass=192
#     print(f"Welcome to {shreelibrary.libarayname} ".upper())
#     print('Do you want to\n 1:List all the books of the library\n 2:Lend of book \n 3:donate a book \n 4:return a book\n 5:Admin pannel\nQ for Exit from the system ')
#     Exit = False
#     while (Exit is not True):
#         firstuser = input("\noption:").capitalize()
#         if firstuser == '1':
#             shreelibrary.listofbook()
#         elif firstuser == '2':
#             shreelibrary.lendbook()
#         elif firstuser == '3':
#             shreelibrary.addbook()
#         elif firstuser == '4':
#             shreelibrary.returnbook()
#         elif firstuser=='5':
#             print("This is for admin only\n")
#             foradmin=int(input("Enter the password:"))
#             if foradmin == adminpass:
#                 shreelibrary.bookdel()
#             else:
#                 print("Access denied")
#         elif firstuser == 'Q':
#             Exit = True
#         else:
#             print(f"Welcome to {shreelibrary.libarayname} ")
# if __name__ == '__main__':
#     main()