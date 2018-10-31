from __future__ import print_function

import platform
import sys
import textwrap
from collections import namedtuple

import os

from consolemenu.validators.base import BaseValidator, InvalidValidator

InputResult = namedtuple("InputResult", "input_string validation_result")


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
        input_string = self._get_input(prompt=prompt)
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

    def _get_input(self, prompt):
        if sys.version[0] == '2':
            return raw_input(prompt)
        else:
            return input(prompt)

    def printf(self, *args):
        print(*args, end='')

    def println(self, *args):
        print(*args)
