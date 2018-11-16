from __future__ import print_function

import platform
import sys
import textwrap
from collections import namedtuple

import os

from consolemenu.validators.base import BaseValidator, InvalidValidator

InputResult = namedtuple("InputResult", "input_string validation_result")


class UserQuit(Exception):
    pass


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

    @staticmethod
    def clear():
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def input(self, prompt='', validators=None, default=None, enable_quit=False, quit_string='q',
              quit_message='(enter q to Quit)'):

        if enable_quit:
            prompt = '{} {}'.format(quit_message, prompt)

        input_string = self._get_input(prompt=prompt)

        if enable_quit and quit_string == input_string:
            raise UserQuit

        if default is not None and input_string == '':
            input_string = default

        validation_result = True

        if isinstance(validators, BaseValidator):
            validators = [validators]
        elif validators is None:
            validators = []

        if isinstance(validators, list):
            validation_results = []
            for validator in validators:
                if isinstance(validator, BaseValidator):
                    validation_results.append(validator.validate(input_string=input_string))
                else:
                    raise InvalidValidator("Validator {} is not a valid validator".format(validator))

            validation_result = all(validation_results)
        else:
            raise InvalidValidator("Validator {} is not a valid validator".format(validators))

        return InputResult(input_string=input_string, validation_result=validation_result)

    @staticmethod
    def _get_input(prompt):
        if sys.version[0] == '2':
            return raw_input(prompt)
        else:
            return input(prompt)

    @staticmethod
    def printf(*args):
        print(*args, end='')

    @staticmethod
    def println(*args):
        print(*args)
