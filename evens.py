def even_number_of_evens(numbers: list) -> bool:
    """
    Checks if there is an even number of even numbers in a list.
    Args:
        numbers (list): List of integers to check.
    Raises:
        TypeError: If the argument is not a list.
    Returns:
        bool: True if the number of even numbers is even and greater than 0, False otherwise.
    """
    if not isinstance(numbers, list):
        raise TypeError("A list was not passed into the function")
    
    evens = sum(1 for n in numbers if n % 2 == 0)
    
    # Return True if evens count is non-zero and even, otherwise False
    return evens > 0 and evens % 2 == 0
