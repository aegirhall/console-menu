from __future__ import print_function

from base_test_case import BaseTestCase
from consolemenu import ConsoleMenu
from consolemenu.format.menu_style import (
    MenuStyle
)
from consolemenu.format.menu_borders import *
from consolemenu.format.menu_padding import MenuPadding
from consolemenu.format.menu_margins import MenuMargins
from consolemenu.items import MenuItem
from consolemenu.menu_component import MenuHeader, MenuTextSection, MenuItemsSection, MenuFooter, MenuPrompt


def print_screen_edge(width=80):
    msg = '{title:{fill}^{width}}'.format(title='simulate screen edges', fill='-', width=(width - 2))
    print('{edge}{msg}{edge}'.format(edge="|", msg=msg))


class TestMenuHeader(BaseTestCase):

    def test_menu_header_ascii_no_titles(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style_type=MenuBorderStyleType.ASCII_BORDER))
        for line in header.generate():
            print(line)

    def test_menu_header_ascii_no_subtitle(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style_type=MenuBorderStyleType.ASCII_BORDER), title="My Title")
        for line in header.generate():
            print(line)

    def test_menu_header_ascii(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style_type=MenuBorderStyleType.ASCII_BORDER),
                            title="My Title", subtitle="My Subtitle")
        for line in header.generate():
            print(line)

    def test_menu_header_ascii_title_centered(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style_type=MenuBorderStyleType.ASCII_BORDER),
                            title="My Centered Title", title_align='center')
        for line in header.generate():
            print(line)

    def test_menu_header_ascii_titles_centered(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style_type=MenuBorderStyleType.ASCII_BORDER),
                            title="My Centered Title", title_align='center',
                            subtitle="My Centered Subtitle", subtitle_align='center')
        for line in header.generate():
            print(line)

    def test_menu_header_ascii_with_bottom_border(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style_type=MenuBorderStyleType.ASCII_BORDER),
                            title="My Title", subtitle="I Should Have a Bottom Border",
                            show_bottom_border=True)
        for line in header.generate():
            print(line)

    def test_menu_header_light_no_titles(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style=LightBorderStyle()))
        for line in header.generate():
            print(line)

    def test_menu_header_light_no_subtitle(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style=LightBorderStyle()), title="My Title")
        for line in header.generate():
            print(line)

    def test_menu_header_light_margins_t1_l4_b0_r4(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(margins=MenuMargins(1, 4, 0, 4),
                                      border_style=LightBorderStyle()),
                            title="My Title")
        for line in header.generate():
            print(line)

    def test_menu_header_light_padding_t3_l4_b3_r4(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(padding=MenuPadding(3, 4, 3, 4),
                                      border_style=LightBorderStyle()),
                            title="My Title")
        for line in header.generate():
            print(line)

    def test_menu_header_light_with_bottom_border(self):
        print_screen_edge()
        header = MenuHeader(MenuStyle(border_style_type=MenuBorderStyleType.LIGHT_BORDER),
                            title="My Title", subtitle="I Should Have a Bottom Border",
                            show_bottom_border=True)
        for line in header.generate():
            print(line)


class TestMenuTextBlock(BaseTestCase):

    def setUp(self):
        self.long_text = "This is my really long text. I can use this text area to place very long \
paragraphs of text, to describe to the user what the menu is for, or even to describe each individual menu option, \
if I think the user is not smart enough to figure all this out on his or her own. I hope this is paragraph \
is long enough to display my multi-line capabilities."

    def test_menu_prologue_ascii(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle())
        for line in pro.generate():
            print(line)

    def test_menu_prologue_ascii_no_text_with_top_border(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(), show_top_border=True)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_ascii_no_text_with_bottom_border(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(), show_bottom_border=True)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_ascii_no_text_with_both_borders(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(), show_top_border=True, show_bottom_border=True)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_ascii_text_with_top_border(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(), text="This is my really good prologue.", show_top_border=True)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_ascii_text_with_bottom_border(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(), text="This is my really good prologue.", show_bottom_border=True)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(border_style=LightBorderStyle()))
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight_with_top_border(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(border_style=LightBorderStyle()), show_top_border=True)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight_centered(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(border_style=LightBorderStyle()),
                              text="My centered prologue.", text_align="center")
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight_long_text_default_margins_and_padding(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(border_style=LightBorderStyle()),
                              text=self.long_text)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight_long_text_big_margins(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(margins=MenuMargins(1, 8, 1, 8), border_style=LightBorderStyle()),
                              text=self.long_text)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight_long_text_big_padding(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(padding=MenuPadding(2, 8, 2, 8), border_style=LightBorderStyle()),
                              text=self.long_text)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight_long_text_big_margins_and_big_padding(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(margins=MenuMargins(1, 8, 1, 8), padding=MenuPadding(2, 8, 2, 8),
                                        border_style=LightBorderStyle()),
                              text=self.long_text)
        for line in pro.generate():
            print(line)

    def test_menu_prologue_unicodelight_long_text_set_via_property(self):
        print_screen_edge()
        pro = MenuTextSection(MenuStyle(border_style=LightBorderStyle()))
        pro.text = self.long_text
        for line in pro.generate():
            print(line)


class TestMenuItemsSection(BaseTestCase):

    def setUp(self):
        self.menu = ConsoleMenu("self.menu", "TestMenuItem")
        self.small_list = [
            MenuItem("menu_item_1", self.menu),
            MenuItem("menu_item_2", self.menu, True),
            MenuItem(text="menu_item_3", menu=self.menu, should_exit=False)
        ]
        self.large_list = [
            MenuItem("menu_item_1", self.menu),
            MenuItem("menu_item_2", self.menu, True),
            MenuItem("menu_item_3", self.menu, True),
            MenuItem("menu_item_4", self.menu, True),
            MenuItem("menu_item_5", self.menu, True),
            MenuItem("menu_item_6", self.menu, True),
            MenuItem("menu_item_7", self.menu, True),
            MenuItem("menu_item_8", self.menu, True),
            MenuItem("menu_item_9", self.menu, True),
            MenuItem("menu_item_10", self.menu, True),
            MenuItem("menu_item_11", self.menu, True),
            MenuItem(text="menu_item_12", menu=self.menu, should_exit=False)
        ]

    def test_menu_items_ascii_no_items(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle())
        for line in sect.generate():
            print(line)

    def test_menu_items_ascii(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(), items=self.small_list)
        for line in sect.generate():
            print(line)

    def test_menu_items_ascii_large_list(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(), items=self.large_list)
        for line in sect.generate():
            print(line)

    def test_menu_items_ascii_padding(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(padding=MenuPadding(1, 4, 1, 4)), items=self.large_list)
        for line in sect.generate():
            print(line)

    def test_menu_items_ascii_margins_and_padding(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(margins=MenuMargins(2, 8, 2, 8), padding=MenuPadding(1, 8, 1, 8)),
                                items=self.small_list)
        for line in sect.generate():
            print(line)

    def test_menu_items_ascii_padding_large_list(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(padding=MenuPadding(1, 4, 1, 4)), items=self.large_list)
        for line in sect.generate():
            print(line)

    def test_menu_items_unicodelight(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(border_style=LightBorderStyle()), items=self.small_list)
        for line in sect.generate():
            print(line)

    def test_show_bottom_border_for_items(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(border_style=LightBorderStyle()), items=self.large_list)
        sect.show_item_bottom_border('menu_item_4', True)
        sect.show_item_bottom_border('menu_item_8', True)
        sect.show_item_bottom_border('menu_item_12', True)
        for line in sect.generate():
            print(line)

    def test_show_top_border_for_items(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(border_style=LightBorderStyle()), items=self.large_list)
        sect.show_item_top_border('menu_item_4', True)
        sect.show_item_top_border('menu_item_8', True)
        sect.show_item_top_border('menu_item_12', True)
        for line in sect.generate():
            print(line)

    def test_show_top_and_bottom_borders_for_items(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(border_style=LightBorderStyle()), items=self.large_list)
        sect.show_item_top_border('menu_item_4', True)
        sect.show_item_bottom_border('menu_item_4', True)
        sect.show_item_top_border('menu_item_8', True)
        sect.show_item_bottom_border('menu_item_8', True)
        sect.show_item_top_border('menu_item_12', True)
        sect.show_item_bottom_border('menu_item_12', True)
        for line in sect.generate():
            print(line)

    def test_show_both_borders_for_items_then_disable_borders(self):
        print_screen_edge()
        sect = MenuItemsSection(MenuStyle(border_style=LightBorderStyle()), items=self.large_list)
        sect.show_item_top_border('menu_item_4', True)
        sect.show_item_bottom_border('menu_item_4', True)
        sect.show_item_top_border('menu_item_8', True)
        sect.show_item_bottom_border('menu_item_8', True)
        sect.show_item_top_border('menu_item_12', True)
        sect.show_item_bottom_border('menu_item_12', True)
        print("This should show top and bottom borders on items 4, 8, and 12")
        for line in sect.generate():
            print(line)
        sect.show_item_top_border('menu_item_4', False)
        sect.show_item_bottom_border('menu_item_4', False)
        sect.show_item_top_border('menu_item_8', False)
        sect.show_item_bottom_border('menu_item_8', False)
        sect.show_item_top_border('menu_item_12', False)
        sect.show_item_bottom_border('menu_item_12', False)
        print("This should not show any borders on any item")
        for line in sect.generate():
            print(line)


class TestMenuFooter(BaseTestCase):

    def test_menu_footer_ascii(self):
        footer = MenuFooter(MenuStyle())
        for line in footer.generate():
            print(line)
        print_screen_edge()

    def test_menu_footer_ascii_margins_t8_l8_b4_r8(self):
        footer = MenuFooter(MenuStyle(margins=MenuMargins(8, 8, 4, 8)))
        for line in footer.generate():
            print(line)
        print_screen_edge()

    def test_menu_footer_unicodelight(self):
        footer = MenuFooter(MenuStyle())
        for line in footer.generate():
            print(line)
        print_screen_edge()


class TestMenuPrompt(BaseTestCase):

    def test_ascii_prompt(self):
        footer = MenuFooter(MenuStyle())
        mp = MenuPrompt(MenuStyle())
        for line in footer.generate():
            print(line)
        for line in mp.generate():
            print(line)

    def test_ascii_prompt_no_top_margin(self):
        # Set footer's bottom margin to 0 and prompt's top padding to 0 so prompt is touching bottom of menu.
        footer = MenuFooter(MenuStyle(margins=MenuMargins(0, 2, 0, 2)))
        mp = MenuPrompt(MenuStyle(padding=MenuPadding(0, 1, 1, 1)))
        for line in footer.generate():
            print(line)
        for line in mp.generate():
            print(line)

    def test_unicode_prompt_no_top_margin(self):
        # Set top padding to 0 so prompt is touching bottom of menu.
        style = MenuStyle(padding=MenuPadding(0, 2, 0, 2), border_style=LightBorderStyle())
        footer = MenuFooter(style)
        mp = MenuPrompt(style, prompt_string=u"\u27EB")
        for line in footer.generate():
            print(line)
        for line in mp.generate():
            print(line)
