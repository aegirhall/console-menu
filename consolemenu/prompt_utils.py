import getpass

from collections import namedtuple
from consolemenu.validators.base import BaseValidator, InvalidValidator


InputResult = namedtuple("InputResult", "input_string validation_result")


class PromptFormatter(object):
    """
    Class for formatting a text input prompt, to allow overriding the message as desired.
    """
    @staticmethod
    def format_prompt(prompt=None, default=None, enable_quit=False, quit_string='q',
                      quit_message='(enter q to Quit)'):
        """
        Format the prompt.
        :param prompt: the prompt message.
        :param default:  the default answer if user does not provide a response.
        :param enable_quit: specifies whether the user can cancel out of the input prompt.
        :param quit_string: the string whcih the user must input in order to quit.
        :param quit_message: the message to explain how to quit.
        :return: the formatted prompt string.
        """
        if prompt is None:
            return None
        prompt = prompt.rstrip()
        prompt = prompt.rstrip(':')
        if enable_quit:
            prompt = "{0} {1}".format(prompt, quit_message)
        if default:
            prompt = "{0} [{1}]".format(prompt, default)
        return "{0}: ".format(prompt)


class PromptUtils(object):
    """
    Utility class with various routines for prompting for user input.
    """

    def __init__(self, screen, prompt_formatter=None):
        """
        Creates a new instance of ConsoleUtils with the specified console. If no console was
        specified, creates a new default console using the ConsoleFactory.
        :param console: the console instance.
        :param prompt_formatter: instance of PromptFormatter for displaying the prompt.
        """
        self.__screen = screen
        if prompt_formatter is None:
            prompt_formatter = PromptFormatter()
        self.__prompt_formatter = prompt_formatter

    @property
    def screen(self):
        return self.__screen

    def clear(self):
        """
        Clear the screen.
        """
        self.__screen.clear()

    def confirm_answer(self, answer, message=None):
        """
        Prompts the user to confirm a question with a yes/no prompt.
        If no message is specified, the default message is:  "You entered {}. Is this correct?"
        :param answer: the answer to confirm.
        :param message: a message to display rather than the default message.
        :return: True if the user confirmed Yes, or False if user specified No.
        """
        if message is None:
            message = "\nYou entered {0}.  Is this correct?".format(answer)
        return self.prompt_for_yes_or_no(message)

    def enter_to_continue(self, message=None):
        """
        Creates a console prompt with the given message, or defaults to 'Press [Enter] to continue' if no message
        is provided.
        :param message:
        """
        if message:
            message = message.rstrip() + ' '
        else:
            message = 'Press [Enter] to continue '
        self.__screen.input(message)

    def input(self, prompt=None, default=None, validators=None, enable_quit=False, quit_string='q',
              quit_message='(enter q to Quit)'):
        """
        Prompt the user for input.
        :param prompt: the message to prompt the user.
        :param default: the default value to suggest as an answer.
        :param validators: list of validators to perform input validation.
        :param enable_quit: specifies whether the user can cancel out of the input prompt.
        :param quit_string: the string whcih the user must input in order to quit.
        :param quit_message: the message to explain how to quit.
        :return: an InputResult tuple.
        """

        prompt = self.__prompt_formatter.format_prompt(prompt=prompt, default=default, enable_quit=enable_quit,
                                                       quit_string=quit_string, quit_message=quit_message)

        input_string = self.__screen.input(prompt=prompt)

        if enable_quit and quit_string == input_string:
            raise UserQuit

        if default is not None and input_string.strip() == '':
            input_string = default

        validation_result = self.validate_input(input_string, validators)

        return InputResult(input_string=input_string, validation_result=validation_result)

    def input_password(self, message=None):
        """
        Prompt the user for a password. This is equivalent to the input() method, but does not echo inputted
        characters to the screen.
        :param message: the prompt message.
        """
        message = self.__prompt_formatter.format_prompt(message)
        try:
            if message:
                return getpass.getpass(message)
            else:
                return getpass.getpass()
        except BaseException:
            self.__screen.println('Warning: Unable to mask input; characters will be echoed to console')
            return self.input(message)

    def printf(self, *args):
        """
        Prints the specified arguments to the screen.
        :param args: object or list of objects to be printed.
        """
        self.__screen.printf(*args)

    def println(self, *args):
        """
        Prints the specified arguments to the screen, followed by a newline character.
        :param args: object or list of objects to be printed.
        """
        self.__screen.println(*args)

    def prompt_and_confirm_password(self, message):
        """
        Method to prompt for a password using the given message, then prompt for a confirmation
        password, and verify that they match.
        :param message:  the prompt message
        :return: the password
        """
        while True:
            pwd = self.input_password(message)
            cpwd = self.input_password("Confirm password")
            if pwd == cpwd:
                return pwd
            else:
                self.__screen.cprintln("Passwords do not match.")

    def prompt_for_bilateral_choice(self, prompt, option1, option2):
        """
        Prompt the user for a response that must be one of the two supplied choices.
        NOTE: The user input verification is case-insensitive, but will return the original case provided
        by the given options.
        """
        if prompt is None:
            prompt = ''
        prompt = prompt.rstrip() + ' (' + option1 + '/' + option2 + ')'
        while True:
            user_input = self.__screen.input(prompt)
            if str(user_input).lower() == option1.lower():
                return option1
            elif str(user_input).lower() == option2.lower():
                return option2

    def prompt_for_trilateral_choice(self, prompt, option1, option2, option3):
        """
        Prompt the user for a response that must be one of the three supplied choices.
        NOTE: The user input verification is case-insensitive, but will return the original case provided
        by the given options.
        """
        if prompt is None:
            prompt = ''
        prompt = prompt.rstrip() + ' (' + option1 + '/' + option2 + '/' + option3 + ')'
        while True:
            user_input = self.__screen.input(prompt)
            if str(user_input).lower() == option1.lower():
                return option1
            elif str(user_input).lower() == option2.lower():
                return option2
            elif str(user_input).lower() == option3.lower():
                return option3

    def prompt_for_yes_or_no(self, prompt):
        """
        Prompts the user with the specified question, and expects a yes (y) or no (n)
        response, returning a boolean value representing the user's answer.
        :returns: a boolean value, True for yes, False for no.
        """
        user_input = self.prompt_for_bilateral_choice(prompt, 'y', 'n')
        return user_input == 'y'

    def prompt_for_numbered_choice(self, choices, title=None, prompt=">"):
        """
        Displays a numbered vertical list of choices from the provided list of strings.
        :param choices: list of choices to display
        :param title: optional title to display above the numbered list
        :param prompt: prompt string. Default is ">"
        :return: an int representing the selected index.
        """
        if choices is None or len(choices) < 1:
            raise Exception('choices list must contain at least one element.')

        while True:
            self.clear()

            if title:
                self.screen.println(title + "\n")

            for i in range(0, len(choices)):
                print('   {:<4}{choice}'.format(str(i + 1) + ') ', choice=choices[i]))

            answer = self.screen.input('\n{} '.format(prompt))

            try:
                index = int(answer) - 1
                if 0 <= index < len(choices):
                    return index
            except Exception as e:
                continue

    def validate_input(self, input_string, validators):
        """
        Validate the given input string against the specified list of validators.
        :param input_string: the input string to verify.
        :param validators: the list of validators.
        :raises InvalidValidator if the list of validators does not provide a valid InputValidator class.
        :return: a boolean representing the validation result. True if the input string is valid; False otherwise.
        """
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

        return validation_result


class UserQuit(Exception):
    pass
