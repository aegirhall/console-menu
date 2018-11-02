import itertools

from consolemenu import ConsoleMenu
from consolemenu.items import SubmenuItem


class MultiSelectMenu(ConsoleMenu):
    """
    Console menu that allows the selection of multiple menu items at a single prompt.
    """

    def __init__(self, title=None, subtitle=None, show_exit_option=True, formatter=None,
                 prologue_text=None, epilogue_text=None, ack_item_completion=True):
        """
        Create a new MultiSelectMenu for selecting multiple items per input.
        :param title:  the menu title.
        :param subtitle:  the menu subtitle.
        :param show_exit_option: determines if the exit item should be displayed.
        :param formatter: the menu formatter object for styling the menu.
        :param prologue_text: text to display in the prologue section of the menu.
        :param epilogue_text:  text to display in the epilogue section of the menu.

        """
        super(MultiSelectMenu, self).__init__(title, subtitle, show_exit_option, formatter=formatter,
                                              prologue_text=prologue_text, epilogue_text=epilogue_text)
        self.ack_item_completion = ack_item_completion

    def append_item(self, item):
        """
        Add an item to the end of the menu before the exit item.
        Note that Multi-Select Menus will not allow a SubmenuItem to be added, as multi-select menus
        are expected to be used only for executing multiple actions.
        :param MenuItem item: The item to be added
        :raise TypeError: if the specified MenuIem is a SubmenuItem.
        """
        if isinstance(item, SubmenuItem):
            raise TypeError("SubmentItems cannot be added to a MultiSelectMenu")
        super(MultiSelectMenu, self).append_item(item)

    def process_user_input(self):
        """
        Gets the user input and decides what to do with it.
        This overrides the method in ConsoleMenu to allow for comma-delimited and range inputs.
        """
        user_input = self.screen.input().input_string

        try:
            indexes = self.__parse_range_list(user_input)
            # Subtract 1 from each number for its actual index number
            indexes[:] = [x - 1 for x in indexes if 0 < x < len(self.items) + 1]
            for index in indexes:
                self.current_option = index
                self.select()
        except Exception as e:
            return

    @staticmethod
    def __parse_range(rng):
        parts = rng.split('-')
        if 1 > len(parts) > 2:
            raise ValueError("Bad range: '%s'" % (rng,))
        parts = [int(i) for i in parts]
        start = parts[0]
        end = start if len(parts) == 1 else parts[1]
        if start > end:
            end, start = start, end
        return range(start, end + 1)

    def __parse_range_list(self, rngs):
        return sorted(set(itertools.chain(*[self.__parse_range(rng) for rng in rngs.split(',')])))
