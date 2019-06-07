from base_test_case import BaseTestCase
from consolemenu import ConsoleMenu
from consolemenu.items import MenuItem

title_text = "title"
subtitle_text = "subtitle"
item_title_text = "itemtext"


def menu_title():
    return title_text

def menu_subtitle():
    return subtitle_text

def item_title():
    return item_title_text

class TestDynamicTexts(BaseTestCase):
    def setUp(self):
        super(TestDynamicTexts, self).setUp()
        self.menu = ConsoleMenu(menu_title, menu_subtitle)

    def test_show(self):
        global title_text, subtitle_text, item_title_text
        menu_item = MenuItem(item_title, self.menu)
        self.assertEqual(self.menu.get_title(), "title")
        title_text = "newtitle"
        self.assertEqual(self.menu.get_title(), "newtitle")

        self.assertEqual(self.menu.get_subtitle(), "subtitle")
        subtitle_text = "newsubtitle"
        self.assertEqual(self.menu.get_subtitle(), "newsubtitle")

        self.assertEqual(menu_item.get_text(), "itemtext")
        item_title_text = "newtext"
        self.assertEqual(menu_item.get_text(), "newtext")