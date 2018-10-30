import logging
from abc import ABCMeta, abstractmethod


class BaseValidator(object):
    """
    Validator Base class, each validator should inherit from this one
    """
    __metaclass__ = ABCMeta

    def __init__(self, input_string):
        logging.basicConfig()
        self.log = logging.getLogger(type(self).__name__)
        self.__input_string = input_string

    @property
    def input_string(self):
        return self.__input_string

    @abstractmethod
    def validate(self):
        """

        This function should be implemented in the validators

        :return: True in case validation success / False otherwise
        """
        pass
