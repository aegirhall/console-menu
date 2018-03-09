import sys
from threading import Thread
from consolemenu.screen import Screen

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch


class ThreadedReturnGetter(Thread):

    def __init__(self, function, args=None, kwargs=None):
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        self.return_value = None
        self.function = function
        try:
            super(ThreadedReturnGetter, self).__init__(target=self.get_return_value, args=args, kwargs=kwargs,
                                                       daemon=True)
        except TypeError:
            super(ThreadedReturnGetter, self).__init__(target=self.get_return_value, args=args, kwargs=kwargs)
            self.daemon = True

    def get_return_value(self, *args, **kwargs):
        self.return_value = self.function(*args, **kwargs)


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_screen = Mock(spec=Screen())
        self.mock_screen.input.return_value = 4

        self.patcher = patch(target='consolemenu.console_menu.Screen', new=self.mock_screen)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
