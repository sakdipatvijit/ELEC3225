import unittest
import sqlite3
from Admin import Admin
from Instructor import Instructor
from Student import Student

# Edson Tenorio

class TestCourseSearchFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Connect to the existing database
        cls.conn = sqlite3.connect('School.db')
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.conn.close()

    def setUp(self):
        # This method will be called before each test
        self.admin = Admin("AdminFirstName", "AdminLastName", 1)
        self.instructor = Instructor("InstructorFirstName", "InstructorLastName", 2)
        self.student = Student("StudentFirstName", "StudentLastName", 3)
        
        for user in [self.admin, self.instructor, self.student]:
            user.conn = self.conn  # Inject the test database connection
            user.cursor = self.cursor

        # Add sample data for testing
        self.cursor.execute('INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                            (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3))
        self.conn.commit()

    def tearDown(self):
        # Clean up the database by removing test entries
        self.cursor.execute('DELETE FROM COURSE WHERE CRN IN ("12345")')
        self.conn.commit()

    def test_admin_search_specific_course_by_crn(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.admin.search_specific_course(1, 12345)
        self.assertEqual(expected_course, result)

    def test_admin_search_specific_course_by_department(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.admin.search_specific_course(2, 'Dept')
        self.assertEqual(expected_course, result[0])

    def test_admin_search_specific_course_by_semester(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.admin.search_specific_course(3, 'Fall')
        self.assertEqual(expected_course, result[0])

    def test_instructor_search_specific_course_by_crn(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.instructor.search_specific_course(1, 12345)
        self.assertEqual(expected_course, result)

    def test_instructor_search_specific_course_by_department(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.instructor.search_specific_course(2, 'Dept')
        self.assertEqual(expected_course, result[0])

    def test_instructor_search_specific_course_by_semester(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.instructor.search_specific_course(3, 'Fall')
        self.assertEqual(expected_course, result[0])

    def test_student_search_specific_course_by_crn(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.student.search_specific_course(1, 12345)
        self.assertEqual(expected_course, result)

    def test_student_search_specific_course_by_department(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.student.search_specific_course(2, 'Dept')
        self.assertEqual(expected_course, result[0])

    def test_student_search_specific_course_by_semester(self):
        expected_course = (12345, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', 2024, 3)
        result = self.student.search_specific_course(3, 'Fall')
        self.assertEqual(expected_course, result[0])

if __name__ == "__main__":
    unittest.main()