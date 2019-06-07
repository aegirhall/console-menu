from base_test_case import BaseTestCase
from consolemenu import ConsoleMenu
from consolemenu.items import MenuItem, SubmenuItem

title_text = "title"
subtitle_text = "subtitle"
item_title_text = "itemtext"
submenu_title_text = "mysub"
count = 0


def menu_title():
    return title_text


def menu_subtitle():
    return subtitle_text


def item_title():
    return item_title_text


def submenu_title():
    return submenu_title_text


def my_submenu_function():
    global count
    if count == 0:
        count = count + 1
        return ConsoleMenu("version1")
    else:
        return ConsoleMenu("version2")


class TestDynamicTexts(BaseTestCase):
    def setUp(self):
        super(TestDynamicTexts, self).setUp()
        self.menu = ConsoleMenu(menu_title, menu_subtitle)
        self.first_call = True

    def test_(self):
        global title_text, subtitle_text, item_title_text
        menu_item = MenuItem(item_title, self.menu)

        # Test dynamic change of main menu title
        self.assertEqual(self.menu.get_title(), "title")
        title_text = "newtitle"
        self.assertEqual(self.menu.get_title(), "newtitle")

        # Test dynamic change of main menu subtitle
        self.assertEqual(self.menu.get_subtitle(), "subtitle")
        subtitle_text = "newsubtitle"
        self.assertEqual(self.menu.get_subtitle(), "newsubtitle")

        # Test dynamic menu item text
        self.assertEqual(menu_item.get_text(), "itemtext")
        item_title_text = "newtext"
        self.assertEqual(menu_item.get_text(), "newtext")

        # Test dynamic change of submenu item on each invocation
        submenu_item = SubmenuItem("a_sub", my_submenu_function)
        self.assertEqual(submenu_item.get_submenu().get_title(), "version1")
        self.assertEqual(submenu_item.get_submenu().get_title(), "version2")
