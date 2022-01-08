import sys

from consolemenu import *
from consolemenu.items import *

#
# This example demonstrates dynamic menu text for the menu title, subtitle, and
# a menu item. Also demonstrates dynamically adding/removing the prologue and
# epilogue portions of the menu.
#

version = 1


def root_menu_title():
    """ Returns the text for menu title. """
    global version
    return 'Root Menu v{}'.format(version)


def root_menu_subtitle():
    """ Returns the text for menu subtitle. """
    global version
    return 'This is the Root Menu Subtitle v{}'.format(version)


def menu_item_text():
    """ Returns the text for a dynamically changing menu item. """
    global version
    return 'Menu Item with dynamic text v{}'.format(version)


def increment_version():
    global version
    version += 1


def decrement_version():
    global version
    version -= 1


def add_epilogue(menu):
    menu.epilogue_text = """To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them. To die: to sleep..."""


def remove_epilogue(menu):
    menu.epilogue_text = None


def add_prologue(menu):
    menu.prologue_text = """It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness,
it was the epoch of belief, it was the epoch of incredulity,
it was the season of Light, it was the season of Darkness,
it was the spring of hope, it was the winter of despair."""


def remove_prologue(menu):
    menu.prologue_text = None


def main():
    # Create the root menu, passing functions as arguments for the title and subtitle,
    # rather than static text
    menu = ConsoleMenu(root_menu_title, root_menu_subtitle)

    # These menu items are using static text.
    item1 = FunctionItem("Increment the version", increment_version)
    item2 = FunctionItem("Decrement the version", decrement_version)
    item3 = FunctionItem("Add the Prologue", add_prologue, args=[menu])
    item4 = FunctionItem("Remove the Prologue", remove_prologue, args=[menu])
    item5 = FunctionItem("Add the Epilogue", add_epilogue, args=[menu])
    item6 = FunctionItem("Remove the Epilogue", remove_epilogue, args=[menu])
    item7 = MenuItem("Menu item with static text")

    # menu item with dynamic text, passing a function for the item title rather than static text.
    item8 = MenuItem(menu_item_text)

    # Add all the items to the root menu
    menu.append_item(item1)
    menu.append_item(item2)
    menu.append_item(item3)
    menu.append_item(item4)
    menu.append_item(item5)
    menu.append_item(item6)
    menu.append_item(item7)
    menu.append_item(item8)

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
