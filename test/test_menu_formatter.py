from __future__ import print_function

from base_test_case import BaseTestCase
from consolemenu import ConsoleMenu, MenuFormatBuilder
from consolemenu.format.menu_style import (
    MenuStyle
)
from consolemenu.format.menu_borders import UnicodeLightBorderStyle
from consolemenu.format.menu_padding import MenuPadding
from consolemenu.format.menu_margins import MenuMargins
from consolemenu.items import MenuItem
from consolemenu.menu_component import MenuHeader, MenuTextSection, MenuItemsSection, MenuFooter, MenuPrompt
from consolemenu.screen import Screen


def print_screen_edge(width=80):
    msg = '{title:{fill}^{width}}'.format(title='simulate screen edges', fill='-', width=(width - 2))
    print('{edge}{msg}{edge}'.format(edge="|", msg=msg))


class TestMenuFormatBuilder(BaseTestCase):

    def test_defaults(self):
        screen = Screen()
        print_screen_edge()
        builder = MenuFormatBuilder()
        builder.set_title("This Is My Title").\
            set_subtitle("This is a little subtitle").\
            add_item(MenuItem("This is Item 1")). \
            add_item(MenuItem("This is Item 2")).\
            add_item(MenuItem("This is Item 3"))
        screen.printf(builder.format())

    def test_format_with_prologue_no_border(self):
        screen = Screen()
        builder = MenuFormatBuilder()
        builder.set_title("This Is My Title").\
            set_subtitle("This is a little subtitle").\
            add_item(MenuItem("This is Item 1")). \
            add_item(MenuItem("This is Item 2")).\
            add_item(MenuItem("This is Item 3")).\
            set_prologue_text('This a very long prologue, which can be used to explain how to use this menu, for people that might not understand it.')
        screen.printf(builder.format())

    def test_format_with_prologue(self):
        screen = Screen()
        builder = MenuFormatBuilder()
        builder.set_title("This Is My Title"). \
            set_subtitle("This is a little subtitle"). \
            add_item(MenuItem("This is Item 1")). \
            add_item(MenuItem("This is Item 2")). \
            add_item(MenuItem("This is Item 3")). \
            set_prologue_text("This is my prologue. Follow these instructions.")
        screen.printf(builder.format())

