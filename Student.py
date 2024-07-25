import sqlite3
from User import User

# Establish database connection
database = sqlite3.connect("School.db")
cursor = database.cursor()

class Student(User):
    def __init__(self, first_name_input, last_name_input, ID_input):
        super().__init__(first_name_input, last_name_input, ID_input)

    def add_course(self, CRN):
        # SQL query to fetch the course details
        schedule_query = "SELECT CRN, TITLE FROM COURSE WHERE CRN = ?;"
        cursor.execute(schedule_query, (CRN,))
        course = cursor.fetchone()

        if course is not None:
            # If the course exists, insert it into the student's schedule
            schedule_modify = "INSERT INTO SCHEDULE (CRN, ID) VALUES (?, ?);"
            cursor.execute(schedule_modify, (course[0], self.ID))

            # Commit the transaction to save changes
            database.commit()
            print("Course added successfully.")
        else:
            print("Course not found.")

    def drop_course(self, CRN):
        # SQL query to delete a course from the student's schedule
        schedule_modify = "DELETE FROM SCHEDULE WHERE CRN = ? AND ID = ?;"
        cursor.execute(schedule_modify, (CRN, self.ID))

        # Commit the transaction to save changes
        database.commit()
        print("Course dropped successfully.")

    def print_schedule(self):
        schedule_query = cursor.execute("SELECT * FROM SCHEDULE WHERE ID = ?", (self.ID,)).fetchall()
        for course in schedule_query:
            print(course)

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