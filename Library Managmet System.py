import time
import getpass
class LibraryManagmentSystem:
    def __init__(self) -> None:
        self.books=[]
        self.userName="admin"
        self.password="yourPassword"
    def adminLogin(self):
        while True:
            enterdUserName=input("Enter Username : ")
            enteredPassword=getpass.getpass("Enter password : ")
            if enterdUserName==self.userName and enteredPassword==self.password:
                print("Login Successful!")
                return True
            else:
                print("Entered Invalid Username or Password!!\n\nTry Again....!!!")
    def changePassword(self):
        currentPassword=getpass.getpass("Enter Current Password : ")
        if currentPassword!=self.password:
            print("Incorrect Password")
            return
        
        newPassword=getpass.getpass("Enter New Password : ")
        confirmPassword=getpass.getpass("Confirm New Password : ")
        if newPassword!=confirmPassword:
            print("New Password donot match!!\n\nTry Again!!!...")
            return
        
        self.password=newPassword
        print("Password Changed Successfully")
    def admin(self):
        print("1. Add Books")
        print("2. Issue Books")
        print("3. Edit Books")
        print("4. Return Books")
        print("5. Delete Books")
        print("6. Search Books")
        print("7. Show Books")
        print("8. Change Password")
        print("9. Logout")
        option=input("Enter Option : ")
        if  option=='1':
            self.addBooks()
        elif option=='2':
            self.issueBooks()
        elif option=='3':
            self.editBooks()
        elif option=='4':
           self.returnBooks()
        elif option=='5':
            self.deleteBooks()
        elif option=='6':
            self.searchBooks()
        elif option=='7':
            self.showBooks()
        elif option=='8':
            self.changePassword()
        elif option=='9':
            self.logOut()
        else:
            print("Invalid Option")
    def addBooks(self):
        tittle=input("Enter Book Tittle : ")
        author=input("Enter Book Author : ")
        year=input("Enter Year of Publication(Optional) : ")
        isbn=input("Enter Book ISBN(Optional) : ")
        bookInfo={
            "Tittle ":tittle,
            "Author ":author,
            "Year ":year if year else None,
            "ISBN ":isbn if isbn else None1
        }
        self.books.append(bookInfo)
        print("Book Added Sucessfully!..")
    def issueBooks(self):
        if not self.books:
            print("No Books Available")
            return
        bookTittle=input("Enter tittle of Book to Issue : ")
        issuedBook=[book for book in self.books if book['tittle'].lower()==bookTittle.lower()]
        if issuedBook:
            print(f"Book '{issuedBook[0]['tittle']}' issued Book Sucessfully!!...")
    def editBooks(self):
        if not self.books:
            print("No Books available to edit")
            return
        print("Edit Books")
        booktittle=input("Enter Tittle of Book to Edit : ")
        bookToEdit=[book for book in self.books if book['tittle'].lower()==booktittle.lower()]
        if bookToEdit:
            book=bookToEdit[0]
            print(f"Book Editing : {book['tittle']}")
        newTittle=input("Enter New Book Tittle :")
        newAuthor=input("Enter New Book Author :")
        if newTittle:
            book["tittle"]=newTittle
        if newAuthor:
            book["author"]=newAuthor
            print("Book Edited Sucessfully")
        else:
            print("Book not Found")
    def returnBooks(self):
        if not self.books:
            print("No Books Borrowed to return")
            return
        print("Return Books")
        bookTittle=input("Enter Tittle of Book to Return")
        bookToReturn=[book for book in self.book if book['tittle'].lower()==bookTittle.lower()]
        if bookToReturn:
            book=bookToReturn[0]
            print(f"Book Returning : {book['tittle']}")
            confirmReturn=input("Confirm Return(Y/N) : ").lower()
            if confirmReturn=='y':
                print("Book returned Sucessfully")
            else:
                print("Book Return Cancel")
    def deleteBooks(self):
        if not self.books:
            print("No Books Available to delete")
            return
        print("Delete Books")
        bookTittle=input("Enter Tittle of Book to Delete : ")
        bookToDelete=[book for book in self.books if book['tittle'].lower()==bookTittle.lower()]
        if bookToDelete:
            book=bookToDelete[0]
            print(f"Book Deleting : {book['tittle']}")
            confirmDelete=input("Confirm Delete(Y/N) : ").lower()
            if confirmDelete=='y':
                self.books.remove(book)
                print("Book Deleted Sucessfully")
            else:
                print("Book Deletation Cancelled")
        else:
            print("Book not Found")
    def searchBooks(self):
        if not self.books:
            print("No Books Available to Search")
            return
        print("Search Books")
        bookTittle=input("Enter Book Tittle to Search")
        bookToSearch=[book for book in self.book if search_term in book['tittle'].lower() 
                                                 or search_term in book.get('author',"").lower() 
                                                 or search_term in book.get('isbn',"").lower()]
        if bookToSearch:
            print("Search Results:")
            for book in search_result:
                print(f"- Tittle : {book['tittle']},Author : {book['author']}")
                if book.get("year"):
                    print(f"  Year :{book['year']}")
                if book.get("isbn"):
                    print(f"  ISBN :{book['isbn']}")
        else:
            print("No Books Found Matching your search Term")

    def showBooks(self):
        if self.books:
            print("List of Books")
            for book in self.books:
                print(f"-Tittle : {book['tittle']},Author : {book['author']}")
                if book.get("year"):
                    print(f"-Year : {book['year']}")
                if book.get("isbn"):
                    print(f"-Year : {book['isbn']}")
    def logOut(self):
        print("Logging Out")
        time.sleep(5)
        exit()
    def dashBoard(self):
        if self.adminLogin():
            self.admin()
        else:
            print("Exiting the Program")
LMS=LibraryManagmentSystem()
LMS.dashBoard()