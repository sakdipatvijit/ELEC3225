import sqlite3
from User import User  # Import base class

# Establish database connection
database = sqlite3.connect("School.db")
cursor = database.cursor()

class Instructor(User):
    def __init__(self, first_name_input, last_name_input, ID_input):
        super().__init__(first_name_input, last_name_input, ID_input)

    def print_roster(self):
        print(f"Fetching roster for instructor ID: {self.ID}")  # Debug statement

        # Fetch roster details where the instructor ID matches
        roster_query = cursor.execute("SELECT CRN, TITLE FROM ROSTER WHERE ID = ?", (self.ID,)).fetchall()

        if not roster_query:
            print("No courses found for this instructor.")  # Debug statement
            return

        for roster in roster_query:
            print(f"Course: {roster[1]} (CRN: {roster[0]})")
            schedule_query = cursor.execute("SELECT ID FROM SCHEDULE WHERE CRN = ?", (roster[0],)).fetchall()
            if not schedule_query:
                print(f"No students found for course {roster[1]} (CRN: {roster[0]})")  # Debug statement
            for schedule in schedule_query:
                student_query = cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM STUDENT WHERE ID = ?", (schedule[0],)).fetchall()
                print(f"Student: {student_query}")


    def search_course(self):

        course_query = cursor.execute("SELECT * FROM COURSE").fetchall()
        for course in course_query:
            print(course)

    def search_specific_course(self, option, input):

        course_results = []

        if option == '1':
            course = cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (input,)).fetchall()
            print(course)
        elif option == '2':
            course_query = cursor.execute("SELECT * FROM COURSE WHERE DEPARTMENT = ?", (input,)).fetchall()
            for course in course_query:
                print(course)
                course_results.append(course)
        elif option == '3':
            course_query = cursor.execute("SELECT * FROM COURSE WHERE SEMESTER = ?", (input,)).fetchall()
            for course in course_query:
                print(course)
                course_results.append(course)
        else:
            print("Invalid option.")
            return 