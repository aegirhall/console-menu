from __future__ import print_function

from base_test_case import BaseTestCase
from consolemenu import ConsoleMenu, MenuFormatBuilder
from consolemenu.format.menu_style import (
    MenuStyle
)
from consolemenu.format.menu_borders import LightBorderStyle
from consolemenu.format.menu_padding import MenuPadding
from consolemenu.format.menu_margins import MenuMargins
from consolemenu.items import MenuItem
from consolemenu.menu_component import MenuHeader, MenuTextSection, MenuItemsSection, MenuFooter, MenuPrompt
from consolemenu.screen import Screen


def print_screen_edge(width=80):
    msg = '{title:{fill}^{width}}'.format(title='simulate screen edges', fill='-', width=(width - 2))
    print('{edge}{msg}{edge}'.format(edge="|", msg=msg))


class TestMenuFormatBuilder(BaseTestCase):

    def test_empty(self):
        Screen().printf(MenuFormatBuilder().format())

    def test_defaults(self):
        print_screen_edge()
        format = MenuFormatBuilder()
        items = [MenuItem("This is Item 1"),
                 MenuItem("This is Item 2"),
                 MenuItem("This is Item 3")]
        Screen().printf(format.format(title="This is My Title",
                                      subtitle="This is My Little Subtitle",
                                      items=items))

    def test_format_with_prologue_no_border(self):
        format = MenuFormatBuilder()
        items = [MenuItem("This is Item 1"),
                 MenuItem("This is Item 2"),
                 MenuItem("This is Item 3")]
        prologue_text = 'This a very long prologue, which can be used to explain how to use this menu, \
for people that might not understand it.'
        Screen().printf(format.format(title="This is My Title", subtitle="This is My Subtitle",
                                      items=items, prologue_text=prologue_text))

    def test_format_with_header_bottom_border_and_prologue_top_border(self):
            format = MenuFormatBuilder().show_header_bottom_border(True).show_prologue_top_border(True)
            items = [MenuItem("This is Item 1"),
                     MenuItem("This is Item 2"),
                     MenuItem("This is Item 3")]
            prologue_text = 'This a very long prologue, which can be used to explain how to use this menu, \
    for people that might not understand it.'
            Screen().printf(format.format(title="This is My Title", subtitle="This is My Subtitle",
                                          items=items, prologue_text=prologue_text))

    def test_format_with_prologue_with_top_border(self):
        format = MenuFormatBuilder().show_prologue_top_border(True)
        items = [MenuItem("This is Item 1"),
                 MenuItem("This is Item 2"),
                 MenuItem("This is Item 3")]
        prologue_text = "This is my prologue. Follow these instructions."
        Screen().printf(format.format(title="This is My Title", subtitle="This is My Subtitle",
                                      items=items, prologue_text=prologue_text))

    def test_format_with_prologue_with_top_and_bottom_borders(self):
        format = MenuFormatBuilder().show_prologue_top_border(True).show_prologue_bottom_border(True)
        items = [MenuItem("This is Item 1"),
                 MenuItem("This is Item 2"),
                 MenuItem("This is Item 3")]
        prologue_text = "This is my prologue. Follow these instructions."
        Screen().printf(format.format(title="This is My Title", subtitle="This is My Subtitle",
                                      items=items, prologue_text=prologue_text))

    def test_format_with_long_prologue_with_both_borders(self):
        format = MenuFormatBuilder().show_prologue_top_border(True).show_prologue_bottom_border(True)
        items = [MenuItem("This is Item 1"),
                 MenuItem("This is Item 2"),
                 MenuItem("This is Item 3")]
        prologue_text = 'This a very long prologue, which can be used to explain how to use this menu, \
for people that might not understand it. But if they read this description it can help them. Also, I have both \
my top and bottom borders enabled, so you should see them.'
        Screen().printf(format.format(title="This is My Title", subtitle="This is My Subtitle",
                                      items=items, prologue_text=prologue_text))

    def test_format_with_item_borders(self):
        format = MenuFormatBuilder()
        item1 = MenuItem("This is Item 1")
        item2 = MenuItem("This is Item 2")
        item3 = MenuItem("This is Item 3")
        format.show_item_top_border(item2, True)
        format.show_item_bottom_border(item2, True)
        print("This should show both top and bottom borders on item 2...")
        Screen().printf(format.format(title="This is My Title", subtitle="This is My Subtitle",
                                      items=[item1, item2, item3]))
        # Now turn off the borders
        format.show_item_top_border(item2, False)
        format.show_item_bottom_border(item2, False)
        print("This should NOT show any borders on item 2...")
        Screen().printf(format.format(title="This is My Title", subtitle="This is My Subtitle",
                                      items=[item1, item2, item3]))
