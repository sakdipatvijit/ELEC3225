import sqlite3
from User import User  # Import base class

# Establish database connection
database = sqlite3.connect("School.db")
cursor = database.cursor()

class Admin(User):
    def __init__(self, first_name_input, last_name_input, ID_input):
        super().__init__(first_name_input, last_name_input, ID_input)

    def add_course(self, CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT):

        # SQL query to insert a new course
        course_modify = "INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(course_modify, (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT))

        # Commit the transaction to save changes
        database.commit()
        print("Course added successfully.")

    def remove_course(self, CRN):

        # SQL query to delete a course based on CRN
        course_modify = "DELETE FROM COURSE WHERE CRN=?;"
        cursor.execute(course_modify, (CRN,))

        # Commit the transaction to save changes
        database.commit()
        print("Course removed successfully.")


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