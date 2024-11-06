from datetime import date, timedelta
import requests

class Student:
    """
    A class representing a student with methods to manage their course schedule and profile.
    """

    BASE_SCHEDULE_URL = "https://company.com/course-schedule"

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self._naughty_list = False

    @property
    def full_name(self) -> str:
        """
        Returns the student's full name.
        """
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self) -> str:
        """
        Returns the student's email address in a standard format.
        """
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self) -> None:
        """
        Marks the student on the naughty list.
        """
        self._naughty_list = True

    @property
    def is_on_naughty_list(self) -> bool:
        """
        Returns True if the student is on the naughty list.
        """
        return self._naughty_list

    def apply_extension(self, days: int) -> None:
        """
        Extends the end date by a specified number of days.
        """
        self.end_date += timedelta(days=days)

    def course_schedule(self) -> str:
        """
        Fetches the course schedule for the student.
        
        Returns:
            str: The course schedule or an error message if the request fails.
        """
        response = requests.get(f"{self.BASE_SCHEDULE_URL}/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        return "Something went wrong"
