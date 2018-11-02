import getpass


class PromptUtils(object):
    """
    Utility class with varous routines for prompting for user input.
    """

    def __init__(self, screen):
        """
        Creates a new instance of ConsoleUtils with the specified console. If no console was
        specified, creates a new default console using the ConsoleFactory.
        :param console: the console instance.
        """
        self.__screen = screen

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

    @staticmethod
    def format_prompt(message=None, default=None):
        """
        Format the prompt.
        """
        if message is None:
            return None
        message = message.rstrip()
        message = message.rstrip(':')
        if default:
            message = "{0} [{1}]".format(message, default)
        return "{0}: ".format(message)

    def input(self, message=None, default=None):
        """
        Prompt the user for input.
        :param message: the message to prompt the user.
        :param default: the default value to suggest as an answer.
        """
        message = self.format_prompt(message, default)

        user_input = self.__screen.input(message)

        # if user gave us input, return it. if no input but we have a default value,
        # return the default value. if no input and no default, return empty string.
        if user_input is not None and user_input.strip() != '':
            return user_input
        elif default:
            return default
        else:
            return ''

    def input_password(self, message=None):
        """
        Prompt the user for a password. This is equivalent to the input() method, but does not echo inputted
        characters to the screen.
        :param message: the prompt message.
        """
        message = self.format_prompt(message)
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
