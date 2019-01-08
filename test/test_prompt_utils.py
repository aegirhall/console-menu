from __future__ import print_function

import unittest

from mock import Mock, patch

from consolemenu import Screen, PromptUtils
from consolemenu import UserQuit
from consolemenu.validators.base import InvalidValidator
from consolemenu.validators.regex import RegexValidator
from consolemenu.validators.url import UrlValidator


class PromptUtilsTest(unittest.TestCase):

    def setUp(self):
        self.mock_screen = Mock(spec=Screen())
        self.mock_screen.input.return_value = 4

    def test_prompt_for_numbered_choice_list(self):
        prompt_utils = PromptUtils(self.mock_screen)
        choices = [
            'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'option_6',
            'option_7', 'option_8', 'option_9', 'option_10', 'option_11', 'option_12'
        ]
        # Test for input of 1
        self.mock_screen.input.return_value = 1
        selected = prompt_utils.prompt_for_numbered_choice(choices)
        self.assertEqual(0, selected)
        self.assertEqual('option_1', choices[selected])

        # Test for input of 3
        self.mock_screen.input.return_value = 3
        selected = prompt_utils.prompt_for_numbered_choice(choices)
        self.assertEqual(2, selected)
        self.assertEqual('option_3', choices[selected])

        # Test for input of 7
        self.mock_screen.input.return_value = 7
        selected = prompt_utils.prompt_for_numbered_choice(choices)
        self.assertEqual(6, selected)
        self.assertEqual('option_7', choices[selected])

    def test_enter_to_continue(self):
        prompt_utils = PromptUtils(self.mock_screen)
        self.mock_screen.input.return_value = "\n"

        print('First, using the default message...')
        prompt_utils.enter_to_continue()

        print('Now using the specified message...')
        prompt_utils.enter_to_continue('My custom prompt     ')

    def test_prompt_for_bilateral_choice(self):
        prompt_utils = PromptUtils(self.mock_screen)

        self.mock_screen.input.return_value = "yes"
        answer = prompt_utils.prompt_for_bilateral_choice('Please enter a value', 'yes', 'no')
        self.assertEqual('yes', answer)

        self.mock_screen.input.return_value = "Yes"
        answer = prompt_utils.prompt_for_bilateral_choice('Please enter a value', 'yes', 'no')
        self.assertEqual('yes', answer)

        self.mock_screen.input.return_value = "yEs"
        answer = prompt_utils.prompt_for_bilateral_choice('Please enter a value', 'yes', 'no')
        self.assertEqual('yes', answer)

        self.mock_screen.input.return_value = "YES"
        answer = prompt_utils.prompt_for_bilateral_choice('Please enter a value', 'yes', 'no')
        self.assertEqual('yes', answer)

        self.mock_screen.input.return_value = "NO"
        answer = prompt_utils.prompt_for_bilateral_choice('Please enter a value', 'yes', 'no')
        self.assertEqual('no', answer)

        self.mock_screen.input.return_value = "no"
        answer = prompt_utils.prompt_for_bilateral_choice('Please enter a value', 'yes', 'no')
        self.assertEqual('no', answer)

        self.mock_screen.input.return_value = "Y"
        answer = prompt_utils.prompt_for_bilateral_choice('Another prompt, with letters', 'Y', 'N')
        self.assertEqual('Y', answer)

        self.mock_screen.input.return_value = "y"
        answer = prompt_utils.prompt_for_bilateral_choice('Another prompt, with letters', 'Y', 'N')
        self.assertEqual('Y', answer)

        self.mock_screen.input.return_value = "N"
        answer = prompt_utils.prompt_for_bilateral_choice('Another prompt, with letters', 'Y', 'N')
        self.assertEqual('N', answer)

        self.mock_screen.input.return_value = "n"
        answer = prompt_utils.prompt_for_bilateral_choice('Another prompt, with letters', 'Y', 'N')
        self.assertEqual('N', answer)

        self.mock_screen.input.return_value = "e"
        answer = prompt_utils.prompt_for_bilateral_choice('Enable/Disable this setting', 'E', 'D')
        self.assertEqual('E', answer)

        self.mock_screen.input.return_value = "d"
        answer = prompt_utils.prompt_for_bilateral_choice('Enable/Disable this setting', 'E', 'D')
        self.assertEqual('D', answer)

    def test_prompt_for_trilateral_choice(self):
        prompt_utils = PromptUtils(self.mock_screen)

        self.mock_screen.input.return_value = "YES"
        answer = prompt_utils.prompt_for_trilateral_choice('Please enter a value', 'yes', 'no', 'maybe')
        self.assertEqual('yes', answer)

        self.mock_screen.input.return_value = "NO"
        answer = prompt_utils.prompt_for_trilateral_choice('Please enter a value', 'yes', 'no', 'maybe')
        self.assertEqual('no', answer)

        self.mock_screen.input.return_value = "maYbe"
        answer = prompt_utils.prompt_for_trilateral_choice('Please enter a value', 'yes', 'no', 'maybe')
        self.assertEqual('maybe', answer)

        self.mock_screen.input.return_value = "y"
        answer = prompt_utils.prompt_for_trilateral_choice('Another prompt, with letters', 'Y', 'N', 'M')
        self.assertEqual('Y', answer)

        self.mock_screen.input.return_value = "e"
        answer = prompt_utils.prompt_for_trilateral_choice('Enable/Disable/Configure this setting', 'E', 'D', 'C')
        self.assertEqual('E', answer)

        self.mock_screen.input.return_value = "d"
        answer = prompt_utils.prompt_for_trilateral_choice('Enable/Disable/Configure this setting', 'E', 'D', 'C')
        self.assertEqual('D', answer)

        self.mock_screen.input.return_value = "c"
        answer = prompt_utils.prompt_for_trilateral_choice('Enable/Disable/Configure this setting', 'E', 'D', 'C')
        self.assertEqual('C', answer)

    def test_prompt_for_yes_or_no(self):
        prompt_utils = PromptUtils(self.mock_screen)

        self.mock_screen.input.return_value = "y"
        answer = prompt_utils.prompt_for_yes_or_no('Do you want to continue?')
        self.assertTrue(answer)

        self.mock_screen.input.return_value = "n"
        answer = prompt_utils.prompt_for_yes_or_no('Do you want to continue?')
        self.assertFalse(answer)

    def test_input(self):
        prompt_utils = PromptUtils(self.mock_screen)

        # Test the default answer when user just hits enter
        self.mock_screen.input.return_value = "\n"
        res = prompt_utils.input('This is my message with a default', 'default answer')
        self.assertEqual('default answer', res.input_string)

        self.mock_screen.input.return_value = "my_fake_input"
        res = prompt_utils.input('This is my message with no default')
        self.assertEqual('my_fake_input', res.input_string)

    @patch('consolemenu.screen.Screen.input', return_value='This is my Cat')
    def test_input_validation_regex_true(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message', validators=RegexValidator(pattern='.*Cat.*'))
        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'This is my Cat')

    @patch('consolemenu.screen.Screen.input', return_value='This is my Cat')
    def test_input_validation_regex_false(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message', validators=RegexValidator(pattern='Cat'))
        self.assertFalse(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'This is my Cat')

    @patch('consolemenu.screen.Screen.input', return_value='https://www.google.com')
    def test_input_validation_regex_and_url_one_false(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message',
                                          validators=[RegexValidator(pattern='notpresent'), UrlValidator()])
        self.assertFalse(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://www.google.com')

    @patch('consolemenu.screen.Screen.input', return_value='https://www.google.com')
    def test_input_validation_regex_and_url_all_false(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message',
                                          validators=[RegexValidator(pattern='notpresent'), UrlValidator()])
        self.assertFalse(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://www.google.com')

    @patch('consolemenu.screen.Screen.input', return_value='https://asdasd')
    def test_input_validation_emtpy_list(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message', validators=[])
        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://asdasd')

    @patch('consolemenu.screen.Screen.input', return_value='https://asdasd')
    def test_input_validation_invalid_validation(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        with self.assertRaises(InvalidValidator):
            prompt_utils.input(prompt='This is my message', validators=[None])

    @patch('consolemenu.screen.Screen.input', return_value='https://asdasd')
    def test_input_validators_None(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message', validators=None)
        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://asdasd')

    @patch('consolemenu.screen.Screen.input', return_value='')
    def test_input_validators_with_default(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message', validators=UrlValidator(),
                                          default='https://www.google.com')
        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://www.google.com')

    @patch('consolemenu.screen.Screen.input', return_value='q')
    def test_input_quit_enabled_default(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        with self.assertRaises(UserQuit):
            prompt_utils.input(prompt='This is my message', validators=UrlValidator(),
                               default='https://www.google.com', enable_quit=True)

    @patch('consolemenu.screen.Screen.input', return_value='exit')
    def test_input_quit_enabled_none_default(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        with self.assertRaises(UserQuit):
            prompt_utils.input(prompt='This is my message', validators=UrlValidator(),
                               default='https://www.google.com', enable_quit=True, quit_string='exit')

    @patch('consolemenu.screen.Screen.input', return_value='https://www.google.com')
    def test_input_quit_enabled_default_not_quit(self, get_input_mock):
        prompt_utils = PromptUtils(Screen())
        input_result = prompt_utils.input(prompt='This is my message', validators=UrlValidator(),
                                          default='https://www.google.com', enable_quit=True)
        self.assertTrue(input_result.validation_result)
        self.assertEquals(input_result.input_string, 'https://www.google.com')

    @patch('getpass.getpass', return_value='p@ssw0rd')
    def test_input_password(self, mock_getpass):
        prompt_utils = PromptUtils(self.mock_screen)
        ans = prompt_utils.input_password('Enter your password to be masked')
        print('you answered:', ans)
        self.assertEqual('p@ssw0rd', ans)
