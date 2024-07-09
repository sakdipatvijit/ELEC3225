from Student import Student

def test_function_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Remove any surrounding whitespace or newline characters
            line = line.strip()
            # Split the line into action, course_id, and student_id
            action, course_id, student_id = line.split(',')
            # Create a Student instance
            student = Student("FirstName", "LastName", student_id)

            if action == 'ADD':
                student.add_course(course_id)
                print(f"add_course({course_id}) - Course added successfully")

            elif action == 'REMOVE':
                student.drop_course(course_id)
                print(f"drop_course({course_id}) - Course removed successfully")
            else:
                print(f"Unknown action {action} for course_id {course_id}")

# Run the tests using the test cases from the file
if __name__ == "__main__":
    test_function_from_file('test_courses.txt')
