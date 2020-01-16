import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create employees for use in test methods."""
        self.employee1 = Employee('Steve', 'Harrington', 35000)
        self.employee2 = Employee('Nancy', 'Wheeler', 30000)

    def test_give_default_raise(self):
        """Test that the default raise is added correctly."""
        self.employee1.give_raise()
        salary = self.employee1.salary
        self.assertEqual(salary, 40000)

    def test_give_custom_raise(self):
        """Test that a custom raise is added correctly."""
        self.employee2.give_raise(10000)
        salary = self.employee2.salary
        self.assertEqual(salary, 40000)