import sqlite3
from User import User  # Import base class

# Establish database connection
database = sqlite3.connect("School.db")
cursor = database.cursor()

class Admin(User):
    def __init__(self, first_name_input, last_name_input, ID_input):
        super().__init__(first_name_input, last_name_input, ID_input)

    def add_course(self):

        # Collect input for the new course
        CRN = input("Enter CRN: ")
        TITLE = input("Enter Title: ")
        DEPARTMENT = input("Enter Department: ")
        TIME = input("Enter Time: ")
        DAY = input("Enter Day: ")
        SEMESTER = input("Enter Semester: ")
        YEAR = input("Enter Year: ")
        CREDIT = input("Enter Credit: ")

        # SQL query to insert a new course
        course_modify = "INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(course_modify, (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT))

        # Commit the transaction to save changes
        database.commit()
        print("Course added successfully.")

    def remove_course(self):
        # Collect input for the CRN of the course to remove
        CRN = input("Enter CRN: ")

        # SQL query to delete a course based on CRN
        course_modify = "DELETE FROM COURSE WHERE CRN=?;"
        cursor.execute(course_modify, (CRN,))

        # Commit the transaction to save changes
        database.commit()
        print("Course removed successfully.")


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


