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


    def search_specific_course(self, option, input):

        course_results = []

        if option == 1:
            course = cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (input,)).fetchone()
            return course
        elif option == 2:
            course_query = cursor.execute("SELECT * FROM COURSE WHERE DEPARTMENT = ?", (input,)).fetchall()
            for course in course_query:
                print(course)
                course_results.append(course)
        elif option == 3:
            course_query = cursor.execute("SELECT * FROM COURSE WHERE SEMESTER = ?", (input,)).fetchall()
            for course in course_query:
                print(course)
                course_results.append(course)
        else:
            print("Invalid option.")
            return []



