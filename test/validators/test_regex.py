from unittest import TestCase

from consolemenu.validators.base import BaseValidator
from consolemenu.validators.regex import RegexValidator


class RegexValidatorTestCase(TestCase):

    def test_is_child_from_base(self):
        self.assertTrue(issubclass(RegexValidator, BaseValidator))

    def test_validate_match(self):
        regex_validator = RegexValidator(input_string="Cats are smarter than dogs", pattern=r'Cats')
        self.assertTrue(regex_validator.validate())

    def test_validate_do_not_match(self):
        regex_validator = RegexValidator(input_string="Cats are smarter than dogs", pattern=r'Rats')
        self.assertFalse(regex_validator.validate())

    def test_validate_invalid_pattern(self):
        regex_validator = RegexValidator(input_string="Cats are smarter than dogs", pattern=None)
        self.assertFalse(regex_validator.validate())
