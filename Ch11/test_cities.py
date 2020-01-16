import unittest
from city_functions import get_city_name

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does input like 'Santiago, Chile' work?"""
        formatted_string = get_city_name('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities and countries with a population work?"""
        formatted_string = get_city_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_string, 'Santiago, Chile - population 5000000')