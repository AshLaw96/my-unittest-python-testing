import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    """
    Unit tests for even_number_of_evens function.
    """

    def test_raises_type_error_for_non_list_input(self):
        """
        Test if a TypeError is raised when the input is not a list.
        """
        with self.assertRaises(TypeError):
            even_number_of_evens(4)
    
    def test_empty_list_returns_false(self):
        """
        Test if an empty list returns False.
        """
        self.assertFalse(even_number_of_evens([]))
    
    def test_even_number_of_evens_in_list(self):
        """
        Test if the function returns True when there's an even number of even numbers.
        """
        self.assertTrue(even_number_of_evens([2, 4]))
    
    def test_odd_number_of_evens_in_list(self):
        """
        Test if the function returns False when there's an odd number of even numbers.
        """
        self.assertFalse(even_number_of_evens([2]))
    
    def test_no_even_numbers_in_list(self):
        """
        Test if the function returns False when there are no even numbers.
        """
        self.assertFalse(even_number_of_evens([1, 3, 5]))


if __name__ == "__main__":
    unittest.main()
