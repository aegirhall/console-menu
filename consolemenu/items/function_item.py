from consolemenu.items import ExternalItem


class FunctionItem(ExternalItem):
    """
    A menu item to call a Python function
    """

    def __init__(self, text, function, args=None, kwargs=None, menu=None, should_exit=False, menu_char=None):
        """
        :ivar str text: The text shown for this menu item
        :ivar function: The function to be called
        :ivar list args: An optional list of arguments to be passed to the function
        :ivar dict kwargs: An optional dictionary of keyword arguments to be passed to the function
        :ivar ConsoleMenu menu: The menu to which this item belongs
        :ivar bool should_exit: Whether the menu should exit once this item's action is done
        :ivar str menu_char: The character used to select this menu item. Optional - defaults to None.
        """
        super(FunctionItem, self).__init__(text=text, menu=menu, should_exit=should_exit, menu_char=menu_char)

        self.function = function

        if args is not None:
            self.args = args
        else:
            self.args = []
        if kwargs is not None:
            self.kwargs = kwargs
        else:
            self.kwargs = {}

        self.return_value = None

    def action(self):
        """
        This class overrides this method
        """
        self.return_value = self.function(*self.args, **self.kwargs)

    def clean_up(self):
        """
        This class overrides this method
        """
        self.menu.resume()

    def get_return(self):
        """
        :return: The return value from the function call
        """
        return self.return_value
