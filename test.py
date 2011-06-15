#!/usr/bin/env python

"""Unit tests for the USA Today Census API."""

import unittest

from mock import Mock

from usa_today import usa_today
from usa_today import Census


def set_up_method_tests():
    """Cut down on boilerplate setup testing code."""
    usa_today.API_KEY = 'my_fake_api_key'
    usa_today.urlopen = Mock()
    usa_today.json = Mock()


class TestCensusInitialization(unittest.TestCase):

    def setUp(self):
        usa_today.API_KEY = 'my_fake_api_key'

    def test_Census_intialized_with_api_key(self):
        census = Census('my_api_key')
        self.assertEquals(census.api_key, 'my_api_key')

    def test_Census_initialized_without_api_key(self):
        census = Census()
        self.assertEquals(census.api_key, 'my_fake_api_key')


class TestCallApiMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_api_method_fails(self):
        self.assertRaises(TypeError, Census().call_api)

    def test_api_method_with_locations_arg(self):
        Census().call_api('locations')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'locations?api_key=my_fake_api_key')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_api_method_with_multiple_args(self):
        Census().call_api('testing', hello='world')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'testing?api_key=my_fake_api_key&hello=world')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_api_method_with_new_api_key(self):
        Census('new_api_key').call_api('testing', hello='world')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'testing?api_key=new_api_key&hello=world')
        usa_today.urlopen.assert_called_with(expected_url)


class TestLocationMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_locations_method_url(self):
        Census().locations()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'locations?api_key=my_fake_api_key')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_locations_method_with_keypat_arg(self):
        Census().locations('TX')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'locations?api_key=my_fake_api_key&keypat=TX')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_locations_method_with_kwargs(self):
        Census().locations(hello='world')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'locations?api_key=my_fake_api_key&hello=world')
        usa_today.urlopen.assert_called_with(expected_url)


class TestEthnicityMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_ethnicity_method_url(self):
        Census().ethnicity()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'ethnicity?api_key=my_fake_api_key')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_ethnicity_method_with_keypat_arg(self):
        Census().ethnicity('TX')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'ethnicity?api_key=my_fake_api_key&keypat=TX')
        usa_today.urlopen.assert_called_with(expected_url)


class TestHousingMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_housing_method_url(self):
        Census().housing()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'housing?api_key=my_fake_api_key')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_housing_method_with_keypat_arg(self):
        Census().housing('TX')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'housing?api_key=my_fake_api_key&keypat=TX')
        usa_today.urlopen.assert_called_with(expected_url)


class TestPopulationMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_housing_method_url(self):
        Census().population()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'population?api_key=my_fake_api_key')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_population_method_with_keypat_arg(self):
        Census().population('TX')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'population?api_key=my_fake_api_key&keypat=TX')
        usa_today.urlopen.assert_called_with(expected_url)


class TestRaceMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_housing_method_url(self):
        Census().race()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'race?api_key=my_fake_api_key')
        usa_today.urlopen.assert_called_with(expected_url)

    def test_race_method_with_keypat_arg(self):
        Census().race('TX')
        expected_url = ('http://api.usatoday.com/open/census/'
                        'race?api_key=my_fake_api_key&keypat=TX')
        usa_today.urlopen.assert_called_with(expected_url)


if __name__ == '__main__':
    unittest.main()
