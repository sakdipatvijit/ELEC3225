import unittest
import sqlite3
from Admin import Admin

class TestAdminFunctions(unittest.TestCase):

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
        self.admin = Admin("FirstName", "LastName", 1)
        self.admin.conn = self.conn  # Inject the test database connection
        self.admin.cursor = self.cursor

    def tearDown(self):
        # Clean up the database by removing test entries
        self.cursor.execute('DELETE FROM COURSE WHERE CRN IN ("12345", "67890")')
        self.conn.commit()

    def test_add_course(self):
        CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT = '12345', 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', '2023', 3
        self.admin.add_course(CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDIT)
        # Query the database to check if the course was added
        self.cursor.execute('SELECT * FROM COURSE WHERE CRN = ?', (CRN,))
        course = self.cursor.fetchone()
        self.assertIsNotNone(course)
        self.assertEqual(course[1], TITLE)

    def test_remove_course(self):
        CRN = '12345'
        self.admin.add_course(CRN, 'CourseTitle', 'Dept', '10:00-11:00', 'MWF', 'Fall', '2023', 3)
        self.admin.remove_course(CRN)
        # Query the database to check if the course was removed
        self.cursor.execute('SELECT * FROM COURSE WHERE CRN = ?', (CRN,))
        course = self.cursor.fetchone()
        self.assertIsNone(course)

if __name__ == "__main__":
    unittest.main()
