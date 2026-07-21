import json

books = []

# LOAD BOOKS

def load_books():
    global books

    try:
        with open("library.json" , "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []


# SAVE BOOKS

def save_books():
    with open("library.json" , "w") as file:
        json.dump( books , file , indent = 4 )


# ADD BOOKS

def add_books():
    title = input("Enter Book Title : ")
    author = input("Enter Author Name : ")

    book = {
        "title" : title,
        "author" : author

    }
    books.append(book)
    save_books()
    print("Book Added Sucessfully!")


# VIEW BOOKS

def view_books():
    if len(books) == 0:
        print("No Books Avaliable")
        return
    
    print("\n ----- BOOKS -----")

    for book in books:
        print("Title : " , book["title"])
        print("Author : " , book["author"])
        print("-" * 25)


# DELETE BOOK

def delete_book():
    title = input("Enter Book Title To Delete : ").lower()

    for book in books:

        if book ["title"].lower() == title:
            undo_stack.append(book)
            books.remove(book)
            save_books()
            print("Book Deleted Successfully!")
            return
    print("Book Not Found")


# SEARCH BOOK

def search_book():
    title = input("Enter Book Title To Search : ").lower()

    for book in books:
        if book["title"].lower() == title :
            print("\n Book Found")
            print("Title : ",book["title"])
            print("Author : ",book["author"])
            return

    else:
        print("Book Not Found")


# SORT BOOKS

def sort_books():
    n = len(books)

    for i in range(n):
        for j in range(0, n-i-1):

            if books[j] ["title"].lower()>books[j+1] ["title"].lower():
                books[j] , books[j+1] = books[j+1] , books[j]
            
        save_books()
        print("Books Sorted Successfully!")


undo_stack = []
issue_queue = []

# STACK UNDO DELETE 

def undo_delete():
    if len(undo_stack) == 0:
        print("Nothing To Undo")
        return
    book =undo_stack.pop()
    books.append(book)
    save_books()
    print("Books Restored Successfully!")


#QUEUE ISSUE BOOK
def issue_book():
    title = input("Enter Book Title : ").lower()

    for book in books: 
        if book["title"].lower() == title:
            issue_queue.append(book)
            print("Book Added To Issue Queue")
            return
        
    print("Book Not Found")


# VIEW QUEUE

def view_queue():
    if len(issue_queue) == 0 :
        print("Queue Is Empty")
        return
    print("\n Issue Queue")
    
    for book in issue_queue:
        print(book["title"])


# COUNT BOOKS

def count_books(index):
    if index == len(books):
        return 0
    return 1 + count_books(index+1)


#MAIN MENU

def menu ():
    load_books()
    while True:
        print("\n ====== LIBRARY MANAGMENT ======")
        print("1.Add Books")
        print("2.View Books")
        print("3.Delete Book")
        print("4.Search Book")
        print("5.Sort Books")
        print("6.Undo Delete(Stack)")
        print("7.Issue Book(Queue)")
        print("8.View Queue")
        print("9.Count Books(Recursion)")
        print("10.Exit")

        try:

            choice = int(input("Enter Choice : "))

            if choice == 1:
                add_books()

            elif choice == 2:
                view_books()

            elif choice == 3:
                delete_book()

            elif choice == 4:
                search_book()

            elif choice == 5:
                sort_books()

            elif choice == 6:
                undo_delete()

            elif choice == 7:
                issue_book()

            elif choice == 8:
                view_queue()

            elif choice == 9:
                print("Total Books : ",count_books(0))

            elif choice == 10:
                print("Thank You!")
                
                break

            else:
                print("Invalid Choice")
        
        except ValueError :
            print("Enter Numbers Only")

menu()







    

