from unittest import TestCase

from consolemenu.validators.base import BaseValidator
from consolemenu.validators.regex import RegexValidator
from consolemenu.validators.url import UrlValidator


class UrlValidatorTestCase(TestCase):
    def test_is_child_from_base(self):
        self.assertTrue(issubclass(RegexValidator, BaseValidator))

    def test_validate_valid_https(self):
        self.assertTrue(UrlValidator(url='https://www.google.es/').validate())

    def test_validate_valid_http(self):
        self.assertTrue(UrlValidator(url='http://www.google.es/').validate())

    def test_validate_valid_no_ending_slash(self):
        self.assertTrue(UrlValidator(url='https://www.google.es').validate())

    def test_validate_invalid(self):
        self.assertFalse(UrlValidator(url='google').validate())
