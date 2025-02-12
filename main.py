# Importing modules
from tinydb import TinyDB, Query # Module for database operations

#Initialising a database
db = TinyDB('StudentDatabase.json', indent=4) #Create/open a JSON file
User = Query() # Defines a Query object to search the database

#List of valid grades
valid_grades = ['A','B','C','D','F']

# Function to delete a student record
def del_record():
    while True:
        try:
            ID = int(input("Enter the ID of the student you would like to Delete:   "))
            break
        except ValueError:
            print("ID must be an integer!") # Ensures the ID is an integer
    if db.contains(User.ID == ID): # Check if the student exists in the database
        db.remove(User.ID == ID) # Removes the student from the database
        print(f"Removed User")
    else:
        print("No such record exists.")

# Function to edit a student record
def edit_records():
    while True:
        try:
            ID = int(input("Enter the ID of the record to edit:   "))
            break
        except ValueError:
            print("ID must be an integer!") # Ensure the ID is an integer
    if db.contains(User.ID == ID): # Check if the student is in the database
        new_grade = input("What would you like to change the grade to?  ") # Prompts for new grade
        db.update({'grade' : new_grade}, User.ID == ID) # Changes the student's grade to the new one
        print(f"Changed grade to {new_grade}")
    else:
        print("No such user exists.") # Informs the user that the student does not exist

def search_by_grade():
    count=0
    query = input("Enter search query OR press ENTER to count how many students achieved each grade:  ").upper()
    if query != '': # If the user enters a grade
        for item in db:
            if item["grade"] == query: # Check if the database has data matching the query
                count+=1
                print(item)
        if count == 0:
            print("No results returned.")
        else:
            print(f"Total of {count} results returned.")
    else: # If the user just presses enter
        grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for item in db:
            grade = item.get("grade") # Gets each students' grade
            if grade in grade_counts:
                grade_counts[grade] += 1 # Adds 1 to the corresponding grade count
                
        for grade, count in grade_counts.items(): # Displays counts for each grade
            print(f"Grade {grade}: {count} students")

# Function to display all student records
def output_records():
    for item in db:
        print(item)

# Function to add a new student
def add_user():
    valid=False # Variable used to avoid errors 
    grade='' # Variable used to avoid errors
    while True:
        while True:
            try:
                while not valid:
                    ID = int(input("Enter the student ID:   "))
                    if db.contains(User.ID == ID):
                        print("A student already exists with that ID!") # Checks if there is already a student with that ID
                    else:
                        valid=True # Becomes true if the ID is unique
                break
            except ValueError:
                print("ID must be an integer!") # Make sure ID is an integer
        name = input("Enter the student name:   ")
        while True:
            try:
                age = int(input("Enter the student's age:   "))
                break
            except ValueError:
                print("Age must be a number!") # Ensure age is an integer
        while grade.upper() not in valid_grades: # Validate grade input
            grade = input("Enter the student's grade:   ")
            if grade.upper() not in valid_grades:
                print("Must be a valid grade! (A-F)")
        db.insert({'ID' : ID, 'name' : name, 'age' : age, 'grade' : grade.upper()})
        print(f"{name} has been added to the database.")
        break

# Function to display menu 
def menu():
    while True:
        choice = input("Would you like to:\n1. Add item to database\n2. Edit records\n3. Display records\n4. Search students by grade\n5. Delete record\n6. Exit\n")
        if choice == "1":
            add_user()
        elif choice == "2":
            if len(db) == 0:
                print("There are no records.") # Inform user if the database is empty, so no point of editing records
            else:
                edit_records()
        elif choice == "3":
            if len(db) == 0:
                print("There are no records.") # Inform user if the database is empty, so no point of displaying records
            else:
                output_records()
        elif choice == "4":
            if len(db) == 0:
                print("There are no records.") # Inform user if the database is empty, so no point of searching records
            else:
                search_by_grade()
        elif choice == "5":
            if len(db) == 0:
                print("There are no records.") # Inform user if the database is empty, so no point of deleting records
            else:
                del_record()
        elif choice == "6":
            exit() # Exits the program
        else:
            print("Invalid choice!") # Exit loop if input is invalid

# Run the main menu function
menu()