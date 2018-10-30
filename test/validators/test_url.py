from unittest import TestCase

from consolemenu.validators.base import BaseValidator
from consolemenu.validators.url import UrlValidator


class UrlValidatorTestCase(TestCase):
    def test_is_child_from_base(self):
        self.assertTrue(issubclass(UrlValidator, BaseValidator))

    def test_validate_valid_https(self):
        self.assertTrue(UrlValidator().validate(input_string='https://www.google.es/'))

    def test_validate_valid_http(self):
        self.assertTrue(UrlValidator().validate(input_string='http://www.google.es/'))

    def test_validate_valid_no_ending_slash(self):
        self.assertTrue(UrlValidator().validate(input_string='https://www.google.es'))

    def test_validate_invalid(self):
        self.assertFalse(UrlValidator().validate(input_string='google'))
