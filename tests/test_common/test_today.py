"""Testing today module
   
   This is just a sample test module for module today in common package
   For each module, you should define a separate class in a separate file
   Each separate file represents a separate module

   Please note the naming convention of a test file should be test_foo or foo_test to 
   be discovered by pytest.  In this project, we go with the convention of test_foo
"""

from servmon.common import today
from datetime import date
import pytest

class TestToday:
    """Wrapper class for module testing

       Please wrap all the test cases of a module in one class
       Please note that all functions within a class takes self as the 1st parameter
       The general naming convention is TestFoo, where Foo is the module's name
    """
    def test_today(self):
        """Testing today common function in today module 

        Today's date as a date object should be returned
        This is just a sample test case illustrating the use of pytest

        """
        result = today.today()

        #Test if result is equal to date.today()
        assert result == date.today()
