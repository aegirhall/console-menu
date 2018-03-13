import unittest

from consolemenu.screen import Screen


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
