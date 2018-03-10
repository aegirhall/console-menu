from __future__ import print_function

from mock import Mock, patch
import unittest

from consolemenu import Screen, PromptUtils


class PromptUtilsTest(unittest.TestCase):

    def setUp(self):
        self.mock_screen = Mock(spec=Screen())
        self.mock_screen.input.return_value = 4

        '''
        self.patcher = patch(target='consolemenu.PromptUtils', new=self.mock_screen)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
        '''

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
        ans = prompt_utils.input('This is my message with a default', 'default answer')
        self.assertEqual('default answer', ans)

        self.mock_screen.input.return_value = "my_fake_input"
        ans = prompt_utils.input('This is my message with no default')
        self.assertEqual('my_fake_input', ans)

    @patch('getpass.getpass')
    def test_input_password(self, mock_getpass):
        mock_getpass.return_value = "p@ssw0rd"

        prompt_utils = PromptUtils(self.mock_screen)
        ans = prompt_utils.input_password('Enter your password to be masked')
        print('you answered:', ans)
        self.assertEqual('p@ssw0rd', ans)
