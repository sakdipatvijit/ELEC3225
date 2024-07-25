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
            return course_results
        elif option == 3:
            course_query = cursor.execute("SELECT * FROM COURSE WHERE SEMESTER = ?", (input,)).fetchall()
            for course in course_query:
                print(course)
                course_results.append(course)
            return course_results
        else:
            print("Invalid option.")
            return []