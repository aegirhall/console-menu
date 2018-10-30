from __future__ import print_function

import os
import platform
import threading

from consolemenu.menu_formatter import MenuFormatBuilder
from consolemenu.screen import Screen


class ConsoleMenu(object):
    """
    A class that displays a menu and allows the user to select an option

    :cvar ConsoleMenu cls.currently_active_menu: Class variable that holds the currently active menu or None if no menu\
    is currently active (E.G. when switching between menus)
    """
    currently_active_menu = None

    def __init__(self, title=None, subtitle=None, show_exit_option=True, screen=None, formatter=None,
                 prologue_text=None, epilogue_text=None):
        """
        :ivar str title: The title of the menu
        :ivar str subtitle: The subtitle of the menu
        :ivar bool show_exit_option: Whether this menu should show an exit item by default. Can be overridden \
        when the menu is started
        :ivar items: The list of MenuItems that the menu will display
        :vartype items: list[:class:`MenuItem<consolemenu.items.MenuItem>`]
        :ivar ConsoleMenu parent: The parent of this menu
        :ivar ConsoleMenu previous_active_menu: the previously active menu to be restored into the class's \
        currently active menu
        :ivar int current_option: The currently highlighted menu option
        :ivar MenuItem current_item: The item corresponding to the menu option that is currently highlighted
        :ivar int selected_option: The option that the user has most recently selected
        :ivar MenuItem selected_item: The item in :attr:`items` that the user most recently selected
        :ivar returned_value: The value returned by the most recently selected item
        :ivar screen: the screen object associated with this menu
        :ivar formatter: the MenuFormatBuilder instance used to format this menu.
        :ivar prologue_text: Text to include in the "prologue" section of the menu.
        :ivar epilogue_text: Text to include in the "epilogue" section of the menu.
        :ivar normal: the normal text color pair for this menu
        :ivar highlight: the highlight color pair associated with this window
        """

        if screen is None:
            screen = Screen()
        self.screen = screen

        if formatter is None:
            formatter = MenuFormatBuilder()
        self.formatter = formatter

        self.title = title
        self.subtitle = subtitle
        self.prologue_text = prologue_text
        self.epilogue_text = epilogue_text

        self.highlight = None
        self.normal = None

        self.show_exit_option = show_exit_option

        self.items = list()

        self.parent = None

        self.exit_item = ExitItem(menu=self)

        self.current_option = 0
        self.selected_option = -1

        self.returned_value = None

        self.should_exit = False

        self.previous_active_menu = None

        self._main_thread = None

        self._running = threading.Event()

    def __repr__(self):
        return "%s: %s. %d items" % (self.title, self.subtitle, len(self.items))

    @property
    def current_item(self):
        """
        :rtype: MenuItem|None
        """
        if self.items:
            return self.items[self.current_option]
        else:
            return None

    @property
    def selected_item(self):
        """
        :rtype: MenuItem|None
        """
        if self.items and self.selected_option != -1:
            return self.items[self.current_option]
        else:
            return None

    def append_item(self, item):
        """
        Add an item to the end of the menu before the exit item

        :param MenuItem item: The item to be added
        """
        did_remove = self.remove_exit()
        item.menu = self
        self.items.append(item)
        if did_remove:
            self.add_exit()

    def add_exit(self):
        """
        Add the exit item if necessary. Used to make sure there aren't multiple exit items

        :return: True if item needed to be added, False otherwise
        :rtype: bool
        """
        if self.items:
            if self.items[-1] is not self.exit_item:
                self.items.append(self.exit_item)
                return True
        return False

    def remove_exit(self):
        """
        Remove the exit item if necessary. Used to make sure we only remove the exit item, not something else

        :return: True if item needed to be removed, False otherwise
        :rtype: bool
        """
        if self.items:
            if self.items[-1] is self.exit_item:
                del self.items[-1]
                return True
        return False

    def is_selected_item_exit(self):
        """
        Checks to determine if the currently selected item is the Exit Menu item.

        :return: True if the currently selected item is the Exit Menu item; False otherwise.
        :rtype: bool
        """
        return self.selected_item and self.selected_item is self.exit_item

    def _wrap_start(self):
        self._main_loop()
        ConsoleMenu.currently_active_menu = None
        self.clear_screen()
        ConsoleMenu.currently_active_menu = self.previous_active_menu

    def start(self, show_exit_option=None):
        """
        Start the menu in a new thread and allow the user to interact with it.
        The thread is a daemon, so :meth:`join()<consolemenu.ConsoleMenu.join>` should be called if there's a
        possibility that the main thread will exit before the menu is done

        :param bool show_exit_option: Whether the exit item should be shown, defaults to\
        the value set in the constructor
        """

        self.previous_active_menu = ConsoleMenu.currently_active_menu
        ConsoleMenu.currently_active_menu = None

        self.should_exit = False

        if show_exit_option is None:
            show_exit_option = self.show_exit_option

        if show_exit_option:
            self.add_exit()
        else:
            self.remove_exit()

        try:
            self._main_thread = threading.Thread(target=self._wrap_start, daemon=True)
        except TypeError:
            self._main_thread = threading.Thread(target=self._wrap_start)
            self._main_thread.daemon = True

        self._main_thread.start()

    def show(self, show_exit_option=None):
        """
        Calls start and then immediately joins.

        :param bool show_exit_option: Whether the exit item should be shown, defaults to the value set \
        in the constructor
        """
        self.start(show_exit_option)
        self.join()

    def _main_loop(self):
        self._set_up_colors()
        ConsoleMenu.currently_active_menu = self
        self._running.set()

        while self._running.wait() is not False and not self.should_exit:
            self.screen.clear()
            self.draw()
            self.process_user_input()

    def draw(self):
        """
        Refreshes the screen and redraws the menu. Should be called whenever something changes that needs to be redrawn.
        """
        self.screen.printf(self.formatter.format(title=self.title, subtitle=self.subtitle, items=self.items,
                                                 prologue_text=self.prologue_text, epilogue_text=self.epilogue_text))

    def is_running(self):
        """
        :return: True if the menu is started and hasn't been paused
        """
        return self._running.is_set()

    def wait_for_start(self, timeout=None):
        """
        Block until the menu is started

        :param timeout: How long to wait before timing out
        :return: False if timeout is given and operation times out, True otherwise. None before Python 2.7
        """
        return self._running.wait(timeout)

    def is_alive(self):
        """
        :return: True if the thread is still alive, False otherwise
        """
        return self._main_thread.is_alive()

    def pause(self):
        """
        Temporarily pause the menu until resume is called
        """
        self._running.clear()

    def resume(self):
        """
        Sets the currently active menu to this one and resumes it
        """
        ConsoleMenu.currently_active_menu = self
        self._running.set()

    def join(self, timeout=None):
        """
        Should be called at some point after :meth:`start()<consolemenu.ConsoleMenu.start>` to block until
        the menu exits.
        :param Number timeout: How long to wait before timing out
        """
        self._main_thread.join(timeout=timeout)

    def get_input(self):
        """
        Can be overridden to change the input method.
        Called in :meth:`process_user_input()<consolemenu.ConsoleMenu.process_user_input>`

        :return: the ordinal value of a single character
        :rtype: int
        """
        return self.screen.input()

    def process_user_input(self):
        """
        Gets the next single character and decides what to do with it
        """
        user_input = self.get_input()

        try:
            num = int(user_input)
        except Exception:
            return
        if 0 < num < len(self.items) + 1:
            self.current_option = num - 1
            self.select()

        return user_input

    def go_to(self, option):
        """
        Go to the option entered by the user as a number

        :param option: the option to go to
        :type option: int
        """
        self.current_option = option
        self.draw()

    def go_down(self):
        """
        Go down one, wrap to beginning if necessary
        """
        if self.current_option < len(self.items) - 1:
            self.current_option += 1
        else:
            self.current_option = 0
        self.draw()

    def go_up(self):
        """
        Go up one, wrap to end if necessary
        """
        if self.current_option > 0:
            self.current_option += -1
        else:
            self.current_option = len(self.items) - 1
        self.draw()

    def select(self):
        """
        Select the current item and run it
        """
        self.selected_option = self.current_option
        self.selected_item.set_up()
        self.selected_item.action()
        self.selected_item.clean_up()
        self.returned_value = self.selected_item.get_return()
        self.should_exit = self.selected_item.should_exit

    def exit(self):
        """
        Signal the menu to exit, then block until it's done cleaning up
        """
        self.should_exit = True
        self.join()

    def _set_up_colors(self):
        # TODO add color support
        # curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # self.highlight = curses.color_pair(1)
        # self.normal = curses.A_NORMAL
        pass

    def clear_screen(self):
        """
        Clear the screen belonging to this menu
        """
        self.screen.clear()


class MenuItem(object):
    """
    A generic menu item
    """

    def __init__(self, text, menu=None, should_exit=False):
        """
        :ivar str text: The text shown for this menu item
        :ivar ConsoleMenu menu: The menu to which this item belongs
        :ivar bool should_exit: Whether the menu should exit once this item's action is done
        """
        self.text = text
        self.menu = menu
        self.should_exit = should_exit

    def __str__(self):
        return "%s %s" % (self.menu.title, self.text)

    def show(self, index):
        """
        How this item should be displayed in the menu. Can be overridden, but should keep the same signature.

        Default is:

            1 - Item 1

            2 - Another Item

        :param int index: The index of the item in the items list of the menu
        :return: The representation of the item to be shown in a menu
        :rtype: str
        """
        return "%2d - %s" % (index + 1, self.text)

    def set_up(self):
        """
        Override to add any setup actions necessary for the item
        """
        pass

    def action(self):
        """
        Override to carry out the main action for this item.
        """
        pass

    def clean_up(self):
        """
        Override to add any cleanup actions necessary for the item
        """
        pass

    def get_return(self):
        """
        Override to change what the item returns.
        Otherwise just returns the same value the last selected item did.
        """
        return self.menu.returned_value


class ExitItem(MenuItem):
    """
    Used to exit the current menu. Handled by :class:`consolemenu.ConsoleMenu`
    """

    def __init__(self, text="Exit", menu=None):
        super(ExitItem, self).__init__(text=text, menu=menu, should_exit=True)

    def show(self, index):
        """
        This class overrides this method
        """
        if self.menu and self.menu.parent:
            self.text = "Return to %s" % self.menu.parent.title
            # Check if menu title ends with menu. (Some menus will include Menu in the name).
            if not self.text.strip().lower().endswith("menu"):
                self.text += " menu"
        else:
            self.text = "Exit"
        return super(ExitItem, self).show(index)


def clear_terminal():
    """
    Call the platform specific function to clear the terminal: cls on windows, reset otherwise
    """
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('reset')
