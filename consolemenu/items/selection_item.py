from consolemenu.items import MenuItem


class SelectionItem(MenuItem):
    """
    The item type used in :class:`consolemenu.SelectionMenu`
    """

    def __init__(self, text, index, menu=None, menu_char=None):
        """
        :ivar str text: The text shown for this menu item
        :ivar int index: The index of this item in the list used to initialize the :class:`consolemenu.SelectionMenu`
        :ivar ConsoleMenu menu: The menu to which this item belongs
        :ivar str menu_char: The character used to select this menu item. Optional - defaults to None.
        """
        super(SelectionItem, self).__init__(text=text, menu=menu, should_exit=True, menu_char=menu_char)
        self.index = index

    def get_return(self):
        """
        :return: The index of this item in the list of strings
        :rtype: int
        """
        return self.index
