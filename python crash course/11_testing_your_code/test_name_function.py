
"""Import unittest and function we want to test."""
import unittest
from name_function import get_formatted_name

"""Create a class that inherits from unittest.TestCase"""
class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    """Any method that starts with test_ will automatically be run when we run the file"""
    def test_first_last_name(self):
        """Test names like Jim Rohn."""

        """Call the function we want to test and pass arguments"""
        formatted_name = get_formatted_name('jim', 'rohn')
        """assert method to verify that the result received in the expected result"""
        self.assertEqual(formatted_name, 'Jim Rohn')


"""Testing frameworks tend to import test files. Without the following block,
interpreter will excute the file which is not desired in that case.
The following 'if' block looks at the special variable '__name__' which gets
set to '__main__' when the file is directly executed.
So while importing this file now, the following function will not execute automatically.
"""
if __name__ == '__main__':
    unittest.main()