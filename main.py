import sqlite3
from Admin import Admin
from Instructor import Instructor
from Student import Student


authenticated = False

while(True):
    # Connect to the SQLite database
    database = sqlite3.connect("School.db")
    cursor = database.cursor()
    while not authenticated:
        # Login
        print("Login")
        username_input = input("Username: ")
        password_input = input("Password: ")

        # Parameterized query to avoid SQL injection
        cursor.execute("SELECT * FROM CREDENTIAL WHERE username = ?", (username_input,))
        credential = cursor.fetchone()

        if credential:
            db_id, db_username, db_password = credential
            str_id = str(db_id)

            if db_password == password_input:
                # Determine user type and instantiate the appropriate classdowd
                if str_id[0] == '1':
                    cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM ADMIN WHERE ID = ?", (db_id,))
                    user_info = cursor.fetchone()
                    user = Admin(user_info[0], user_info[1], db_id)
                elif str_id[0] == '2':
                    cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM INSTRUCTOR WHERE ID = ?", (db_id,))
                    user_info = cursor.fetchone()
                    user = Instructor(user_info[0], user_info[1], db_id)
                elif str_id[0] == '3':
                    cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM STUDENT WHERE ID = ?", (db_id,))
                    user_info = cursor.fetchone()
                    user = Student(user_info[0], user_info[1], db_id)
                
                print(f"Login Successfully {user_info[0]} {user_info[1]}")
                authenticated = True

            else:
                print("Invalid Credentials. Please try again.")
        else:
            print("Invalid Credentials. Please try again.")

    # Proceed with the rest of the program after successful login
    print("Welcome, you are now logged in.")

    # Main loop for user actions
    while authenticated:
        print("Choose an option:")
        
        if isinstance(user, Admin):
            print("1. Print all courses")
            print("2. Print course based on (CRN, DEPARTMENT, SEMESTER)")
            print("3. Add a course")
            print("4. Remove a course")
            print("5. Logout")
    
            option = input("Option: ")

            if option == '1':
                user.search_course()
            elif option == '2':
                user.search_specific_course()
            elif option == '3':
                # Collect input for the new course
                CRN = input("Enter CRN: ")
                TITLE = input("Enter Title: ")
                DEPARTMENT = input("Enter Department: ")
                TIME = input("Enter Time: ")
                DAY = input("Enter Day: ")
                SEMESTER = input("Enter Semester: ")
                YEAR = input("Enter Year: ")
                CREDIT = input("Enter Credit: ")
                user.add_course(CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT)
            elif option == '4':
                # Collect input for the CRN of the course to remove
                CRN = input("Enter CRN: ")
                user.remove_course()
            elif option == '5':
                print("You have successfully logged out.")
                database.close()
                authenticated = False
            else:
                print("Invalid option. Please try again.")

        elif isinstance(user, Instructor):
            print("1. Print all courses")
            print("2. Print course based on (CRN, DEPARTMENT, SEMESTER)")
            print("3. Print course roster")
            print("4. Logout")
            option = input("Option: ")

            if option == '1':
                user.search_course()
            elif option == '2':
                user.search_specific_course()
            elif option == '3':
                user.print_roster()
            elif option == '4':
                print("You have successfully logged out.")
                database.close()
                authenticated = False
            else:
                print("Invalid option. Please try again.")

        elif isinstance(user, Student):
            print("1. Print all courses")
            print("2. Print course based on (CRN, DEPARTMENT, SEMESTER)")
            print("3. Add a course")
            print("4. Drop a course")
            print("5. Print schedule")
            print("6. Logout")
            option = input("Option: ")

            if option == '1':
                user.search_course()
            elif option == '2':
                user.search_specific_course()
            elif option == '3':
                CRN = input("Enter CRN:")
                user.add_course(CRN)
            elif option == '4':
                user.drop_course()
            elif option == '5':
                user.print_schedule()
            elif option == '6':
                print("You have successfully logged out.")
                database.close()
                authenticated = False


            else:
                print("Invalid option. Please try again.")


