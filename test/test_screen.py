import time
import unittest

from mock import patch

from consolemenu.screen import Screen


class TestScreen(unittest.TestCase):

    def test_clear(self):
        screen = Screen()
        screen.println('Clearing screen...')
        screen.clear()

    @patch('consolemenu.screen.Screen.input', return_value='This is my Cat')
    def test_input(self, get_input_mock):
        input_string = Screen().input(prompt='This is my message')
        self.assertEquals(input_string, 'This is my Cat')

    def test_flush(self):
        screen = Screen()
        # standard printf will buffer, so output won't come until newline
        screen.println('The next line should print all at once...')
        for i in range(0, 40):
            screen.printf('.')
            time.sleep(0.5)
        screen.println()
        # now flush after each dot
        screen.println('The next line should print smoothly...')
        for i in range(0, 40):
            screen.printf('.')
            screen.flush()
            time.sleep(0.5)
        screen.println()

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
        self.assertEqual(40, screen.screen_height)
        self.assertEqual(80, screen.screen_width)
