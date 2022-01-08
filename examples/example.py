import sys

from consolemenu import *
from consolemenu.items import *


def input_handler():
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter an input")
    pu.println("\nYou entered:", result.input_string, "\n")
    pu.enter_to_continue()


def main():
    # Create the root menu
    menu = ConsoleMenu("Root Menu", "This is the Root Menu Subtitle")

    item1 = MenuItem("Item 1")

    # Create a menu item that calls a function
    function_item = FunctionItem("Fun item", input_handler)

    # Create a menu item that calls a system command, based on OS type
    if sys.platform.startswith('win'):
        command_item = CommandItem("Command", 'cmd /c \"echo this is a shell. Press enter to continue." && set /p=\"')
    else:
        command_item = CommandItem("Command", 'sh -c \'echo "this is a shell. Press enter to continue."; read\'')

    # Create a submenu using a Selection Menu, which takes a list of strings to create the menu items.
    submenu = SelectionMenu(["item1", "item2", "item3"], title="Selection Menu",
                            subtitle="These menu items return to the previous menu")

    # Create the menu item that opens the Selection submenu
    submenu_item = SubmenuItem("Submenu item", submenu=submenu)
    submenu_item.set_menu(menu)

    # Create a second submenu, but this time use a standard ConsoleMenu instance
    submenu_2 = ConsoleMenu("Another Submenu Title", "Submenu subtitle.")
    function_item_2 = FunctionItem("Fun item", Screen().input, ["Enter an input: "])
    item2 = MenuItem("Another Item")
    submenu_2.append_item(function_item_2)
    submenu_2.append_item(item2)
    submenu_item_2 = SubmenuItem("Another submenu", submenu=submenu_2)
    submenu_item_2.set_menu(menu)

    # Add all the items to the root menu
    menu.append_item(item1)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)
    menu.append_item(submenu_item_2)

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
