import unittest

from mock import patch

from consolemenu.screen import Screen
from consolemenu.validators.base import InvalidValidator
from consolemenu.validators.regex import RegexValidator
from consolemenu.validators.url import UrlValidator


class TestScreen(unittest.TestCase):

    def test_clear(self):
        screen = Screen()
        screen.println('Clearing screen...')
        screen.clear()

    def test_printf(self):
        screen = Screen()
        screen.printf('single message.')
        screen.printf('this should be on ame line as above. explicit newline: \n')
        screen.printf('this', 'is', 'a', 'list', 'message')
        screen.printf('same line as list message', 'explicit newline: \n')
        screen.printf('this is a %s message.\n' % 'printf-style')
        screen.printf('this is a {0} message.\n'.format('format-style'))

    def test_println(self):
        screen = Screen()
        screen.println('single message.')
        screen.println('this a second line.')
        screen.println('this', 'is', 'a', 'list', 'message')
        screen.println('same is a line with an explicit newline, which should cause an empty space below me.\n')
        screen.println('this is a %s message.' % 'printf-style')
        screen.println('this is a {0} message.'.format('format-style'))

    def test_screen_size(self):
        screen = Screen()
        print('screen height:', screen.screen_height)
        print('screen width:', screen.screen_width)

    @patch('consolemenu.screen.Screen._get_input', return_value='This is my Cat')
    def test_screen_input_validation_regex_true(self, get_input_mock):
        input_result = Screen().input(prompt='This is my message', validators=RegexValidator(pattern='.*Cat.*'))
        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'This is my Cat')

    @patch('consolemenu.screen.Screen._get_input', return_value='This is my Cat')
    def test_screen_input_validation_regex_false(self, get_input_mock):
        input_result = Screen().input(prompt='This is my message', validators=RegexValidator(pattern='Cat'))
        self.assertFalse(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'This is my Cat')

    @patch('consolemenu.screen.Screen._get_input', return_value='https://www.google.com')
    def test_screen_input_validation_regex_and_url_one_false(self, get_input_mock):
        input_result = Screen().input(prompt='This is my message',
                                      validators=[RegexValidator(pattern='notpresent'), UrlValidator()])
        self.assertFalse(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://www.google.com')

    @patch('consolemenu.screen.Screen._get_input', return_value='https://www.google.com')
    def test_screen_input_validation_regex_and_url_all_false(self, get_input_mock):
        input_result = Screen().input(prompt='This is my message',
                                      validators=[RegexValidator(pattern='notpresent'), UrlValidator()])
        self.assertFalse(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://www.google.com')

    @patch('consolemenu.screen.Screen._get_input', return_value='https://asdasd')
    def test_screen_input_validation_emtpy_list(self, get_input_mock):
        input_result = Screen().input(prompt='This is my message',
                                      validators=[])
        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://asdasd')

    @patch('consolemenu.screen.Screen._get_input', return_value='https://asdasd')
    def test_screen_input_validation_invalid_validation(self, get_input_mock):
        with self.assertRaises(InvalidValidator):
            Screen().input(prompt='This is my message', validators=[None])

    @patch('consolemenu.screen.Screen._get_input', return_value='https://asdasd')
    def test_screen_input_validators_None(self, get_input_mock):
        input_result = Screen().input(prompt='This is my message', validators=None)

        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://asdasd')
