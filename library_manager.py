import os
import sys
import csv

choice1 = int(input("Enter '1' if you want to use your pre-made csv file or Enter '2' if you want to make a new csv file: "))

if choice1 == 1:
    FILE_NAME = "library.csv"
elif choice1 == 2:
    dummy = input("Enter the name of your file you want to create: ").strip()
    if not dummy.endswith(".csv"):   
        dummy += ".csv"
    FILE_NAME = dummy
else:
    print("Invalid choice! Defaulting to 'library.csv'.")
    FILE_NAME = "library.csv"
def init_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Title", "Author", "Status"])  

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, "Available"])

    print(f"\nBook '{title}' added successfully!\n")

def list_books():
    with open(FILE_NAME, mode="r") as file:
     reader = list(csv.reader(file))   
     header = reader[0]                
     data = reader[1:]                 

    print("\n===== All Books in Library =====")
    for row in data:
     if row:  
        book_id, title, author, status = row
        print(f"[{book_id}] {title} by {author} ({status})")
    print()


def edit_book():
    book_id = input("Enter Book ID to edit: ")

    with open(FILE_NAME, mode="r") as file:
        reader = list(csv.reader(file))
        header = reader[0]      
        rows = reader[1:]       

    found = False
    for row in rows:
        if row and row[0] == book_id:
            found = True
            print(f"Editing Book: {row}")
            print("1. Edit Title")
            print("2. Edit Author")
            print("3. Change Status (Available/Issued)")
            choice = input("Choose option: ")

            if choice == "1":
                row[1] = input("Enter new Title: ")
            elif choice == "2":
                row[2] = input("Enter new Author: ")
            elif choice == "3":
                row[3] = input("Enter new Status (Available/Issued): ")
            else:
                print("Invalid choice, no changes made.")

    if found:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)   
            writer.writerows(rows)    
        print("\nBook updated successfully!\n")
    else:
        print("\nBook not found!\n")

    

    
def main_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. List All Books")
    print("3. Edit Book")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


def run():
    init_csv()  

    while True:
        choice = main_menu()

        if choice == "1":
            add_book()

        elif choice == "2":
            list_books()

        elif choice == "3":
            edit_book()

        elif choice == "4":
            print("Exiting Library Management System... Goodbye!")
            sys.exit()

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    run()
