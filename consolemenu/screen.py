from __future__ import print_function

import os
import platform
import sys
import textwrap

from consolemenu.validators.base import BaseValidator


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
    def screen_height(self):
        return self.__height

    @property
    def screen_width(self):
        return self.__width

    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def input(self, prompt='', validators=None):
        input_value = self.__get_input(prompt=prompt)
        validation_results = []

        if validators is None:
            validators = []

        if isinstance(validators, list):
            for validator in validators:
                validation_results.append(validator.validate())
        elif isinstance(validators, BaseValidator):
            return validators.validate()

    def __get_input(self, prompt):
        if sys.version[0] == '2':
            return raw_input(prompt)
        else:
            return input(prompt)

    def printf(self, *args):
        print(*args, end='')

    def println(self, *args):
        print(*args)
