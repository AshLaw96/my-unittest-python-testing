import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):
    """
    Unit tests for the Student class methods and properties.
    """

    @classmethod
    def setUpClass(cls):
        print("Setting up the TestStudent class")

    def setUp(self):
        print("Setting up a test case")
        self.student = Student("John", "Doe")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the TestStudent class")

    def tearDown(self):
        print("Tearing down a test case")

    def test_full_name(self):
        """
        Test if the full name is generated correctly.
        """
        print("Testing full_name property")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        """
        Test if alert_santa correctly sets naughty list status.
        """
        print("Testing alert_santa method")
        self.student.alert_santa()
        self.assertTrue(self.student.is_on_naughty_list)

    def test_email(self):
        """
        Test if email property is correctly formatted.
        """
        print("Testing email property")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        """
        Test if the apply_extension method correctly extends end date.
        """
        print("Testing apply_extension method")
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        """
        Test course_schedule with a successful response.
        """
        print("Testing course_schedule with a successful response")
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
            mocked_get.assert_called_once_with("https://company.com/course-schedule/Doe/John")

    def test_course_schedule_failed(self):
        """
        Test course_schedule with a failed response.
        """
        print("Testing course_schedule with a failed response")
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")
            mocked_get.assert_called_once_with("https://company.com/course-schedule/Doe/John")

if __name__ == "__main__":
    unittest.main()
