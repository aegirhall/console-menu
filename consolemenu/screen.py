from __future__ import print_function

import os
import platform
import sys
import textwrap


class Screen(object):
    """
    Class representing a console screen.
    """
    def __init__(self):
        self.__tw = textwrap.TextWrapper()
        # TODO get actual screen size
        self.__height = 40
        self.__width = 80

    @property
    def screen_height(self): return self.__height

    @property
    def screen_width(self): return self.__width

    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def input(self, prompt=''):
        if sys.version[0] == '2':
            return raw_input(prompt)
        else:
            return input(prompt)

    def printf(self, *args):
        print(*args, end='')

    def println(self, *args):
        print(*args)
