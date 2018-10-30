from unittest import TestCase

from consolemenu.validators.base import BaseValidator


class BaseTestCase(TestCase):
    def test_is_abstract(self):
        with self.assertRaises(TypeError):
            BaseValidator()

    def test_validate_is_present(self):
        self.assertIsNotNone(getattr(BaseValidator, 'validate'))
