from Admin import Admin

def test_function_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Remove any surrounding whitespace or newline characters
            line = line.strip()
            # Split the line into action and course details
            parts = line.split(',')
            action = parts[0]

            admin = Admin("FirstName", "LastName", 1)

            if action == 'ADD':
                CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT = parts[1:]
                admin.add_course(CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT)
                print(f"add_course({CRN}, {TITLE}, {DEPARTMENT}, {TIME}, {DAY}, {SEMESTER}, {YEAR}, {CREDIT}) - Course added successfully")

            elif action == 'REMOVE':
                CRN = parts[1]
                admin.remove_course(CRN)
                print(f"remove_course({CRN}) - Course removed successfully")

            else:
                print(f"Unknown action {action}")

# Run the tests using the test cases from the file
if __name__ == "__main__":
    test_function_from_file('test_courses_admin.txt')
