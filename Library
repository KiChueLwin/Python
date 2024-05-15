books=["ProfessionalPractice", "English" , "Programming" , "Networking"]
cmd_list = ("List", "Search", "Register", "Delete", "Exit")



# declaring functions to work 
def list_cmd():
    if len(books) == 0:
        print("There is no book registered in this library!")
    else:
        print("\nList of Books")
        for book in books:
           print(f"[{books.index(book) + 1}] {book}")

def search_cmd():
    search_keyword = input("Enter the book name or book keyword!  :")
    for book in books:
        if search_keyword in book:
            print(f"[{books.index(book) + 1}] {book}")


def register_cmd():
    new_book = input("Enter the book name to Register!  :")
    if new_book in books:
        print("This book is already in the library!")
    else:
        books.append(new_book)
        print("Successfully Saved!")

def delete_cmd():
    book_number = int(input("Enter the book name what you want to delete!  : "))
    confirmation = input(f"Are you sure to delete {books[book_number - 1]}?  Yes or No  :")

    if confirmation == "Yes":
        books.pop(book_number - 1)


while True:
    print("\nMy Library")
    print('..........')
    print("# List")
    print("# Search")
    print("# Register")
    print("# Delete")
    print("# Exit")
    print("...........")
    
    command  = ""
    while not command in cmd_list: 
        command = input("Enter one menu  :")

    if command == "List":
        list_cmd()
    elif command == "Search" :
        search_cmd()
    elif command == "Register" :
        register_cmd()
    elif command == "Delete":
        delete_cmd()
    elif command == "Exit":
        break 
