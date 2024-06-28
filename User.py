import sqlite3

# Establish database connection
database = sqlite3.connect("School.db")
cursor = database.cursor()

class User:
    def __init__(self, first_name_input, last_name_input, ID_input):
        self.first_name = first_name_input
        self.last_name = last_name_input
        self.ID = ID_input

    def print_info(self):
        print(f"User info: {self.first_name} {self.last_name} ({self.ID})")

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



