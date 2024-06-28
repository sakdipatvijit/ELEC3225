import sqlite3
from User import User  # Import base class

# Establish database connection
database = sqlite3.connect("School.db")
cursor = database.cursor()

class Instructor(User):
    def __init__(self, first_name_input, last_name_input, ID_input):
        super().__init__(first_name_input, last_name_input, ID_input)

    def print_roster(self):
  
        roster_query = cursor.execute("SELECT * FROM ROSTER").fetchall()
        for roster in roster_query:
            print(roster)


    def search_course(self):

        course_query = cursor.execute("SELECT * FROM COURSE").fetchall()
        for course in course_query:
            print(course)

    def search_specific_course(self):
        print("Search specific course:")
        print("1. CRN")
        print("2. Department")
        print("3. Semester")
        option = input("Enter option: ")


        if option == '1':
            crn_input = input("Enter CRN: ")
            course_query = cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn_input,)).fetchall()
        elif option == '2':
            department_input = input("Enter Department: ")
            course_query = cursor.execute("SELECT * FROM COURSE WHERE DEPARTMENT = ?", (department_input,)).fetchall()
        elif option == '3':
            semester_input = input("Enter Semester: ")
            course_query = cursor.execute("SELECT * FROM COURSE WHERE SEMESTER = ?", (semester_input,)).fetchall()
        else:
            print("Invalid option.")
            return

