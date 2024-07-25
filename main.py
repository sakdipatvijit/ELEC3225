import sqlite3
from Admin import Admin
from Instructor import Instructor
from Student import Student

def login_user(username_input, password_input, cursor):
    cursor.execute("SELECT * FROM CREDENTIAL WHERE username = ?", (username_input,))
    credential = cursor.fetchone()

    if credential:
        db_id, db_username, db_password = credential
        if db_password == password_input:
            if str(db_id)[0] == '1':
                cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM ADMIN WHERE ID = ?", (db_id,))
                user_info = cursor.fetchone()
                return Admin(user_info[0], user_info[1], db_id)
            elif str(db_id)[0] == '2':
                cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM INSTRUCTOR WHERE ID = ?", (db_id,))
                user_info = cursor.fetchone()
                return Instructor(user_info[0], user_info[1], db_id)
            elif str(db_id)[0] == '3':
                cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM STUDENT WHERE ID = ?", (db_id,))
                user_info = cursor.fetchone()
                return Student(user_info[0], user_info[1], db_id)
        else:
            print("Invalid Credentials. Please try again.")
    else:
        print("Invalid Credentials. Please try again.")
    
    return None


authenticated = False

while not authenticated:
    
    # Connect to the SQLite database
    database = sqlite3.connect("School.db")
    cursor = database.cursor()
    
    # Login
    print("Login")
    username_input = input("Username: ")
    password_input = input("Password: ")

    user = login_user(username_input, password_input, cursor)

    if user:
        print(f"Login Successfully {user.first_name} {user.last_name}")

        # Proceed with the rest of the program after successful login
        print("Welcome, you are now logged in.")

        authenticated = True
    else:
        print("Authentication failed. Please try again.")

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
                print("Search specific course:")
                print("1. CRN")
                print("2. Department")
                print("3. Semester")
                specific_option = input("Enter option: ")
                
                if specific_option == '1':
                    specific_input = input("Enter CRN: ")
                elif specific_option == '2':
                    specific_input = input("Enter Department: ")
                elif specific_option == '3':
                    specific_input = input("Enter Semester: ")
                else:
                    print("Invalid option.")
                user.search_specific_course(specific_option, specific_input)
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
                user.remove_course(CRN)
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
                print("Search specific course:")
                print("1. CRN")
                print("2. Department")
                print("3. Semester")
                specific_option = input("Enter option: ")
                
                if specific_option == '1':
                    specific_input = input("Enter CRN: ")
                elif specific_option == '2':
                    specific_input = input("Enter Department: ")
                elif specific_option == '3':
                    specific_input = input("Enter Semester: ")
                else:
                    print("Invalid option.")
                user.search_specific_course(specific_option, specific_input)
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
                print("Search specific course:")
                print("1. CRN")
                print("2. Department")
                print("3. Semester")
                specific_option = input("Enter option: ")
                
                if specific_option == '1':
                    specific_input = input("Enter CRN: ")
                elif specific_option == '2':
                    specific_input = input("Enter Department: ")
                elif specific_option == '3':
                    specific_input = input("Enter Semester: ")
                else:
                    print("Invalid option.")
                user.search_specific_course(specific_option, specific_input)
            elif option == '3':
                CRN = input("Enter CRN:")
                user.add_course(CRN)
            elif option == '4':
                CRN = input("Enter CRN:")
                user.drop_course(CRN)
            elif option == '5':
                user.print_schedule()
            elif option == '6':
                print("You have successfully logged out.")
                database.close()
                authenticated = False

            else:
                print("Invalid option. Please try again.")

