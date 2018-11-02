import sys

from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *


def main():
    # Change some menu formatting
    menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt("SELECT>") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

    menu = ConsoleMenu("Root Menu", "This is the Root Menu Subtitle", formatter=menu_format)
    item1 = MenuItem("Item 1", menu)

    # Create a menu item that calls a function
    function_item = FunctionItem("Fun item", Screen().input, kwargs={"prompt": "Enter an input: "})

    # Create a menu item that calls a system command, based on OS type
    if sys.platform.startswith('win'):
        command_item = CommandItem("Command", 'cmd /c \"echo this is a shell. Press enter to continue." && set /p=\"')
    else:
        command_item = CommandItem("Command", 'sh -c \'echo "this is a shell. Press enter to continue."; read\'')

    # Create a submenu using a Selection Menu, which takes a list of strings to create the menu items. This
    # submenu is passed the same formatter object, to keep its formatting consistent.
    submenu = SelectionMenu(["item1", "item2", "item3"], title="Selection Menu",
                            subtitle="These menu items return to the previous menu",
                            formatter=menu_format)
    # Create the menu item that opens the Selection submenu
    submenu_item = SubmenuItem("Submenu item", submenu=submenu)
    submenu_item.set_menu(menu)

    # Create a different formatter for another submenu, so it has a different look
    submenu_formatter = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.ASCII_BORDER)

    # Create a second submenu, but this time use a standard ConsoleMenu instance, and use the submenu_formatter.
    submenu_2 = ConsoleMenu("Another Submenu Title", "Submenu subtitle. Notice this menu is ASCII.",
                            formatter=submenu_formatter)
    function_item_2 = FunctionItem("Fun item", Screen().input, ["Enter an input: "])
    item2 = MenuItem("Another Item")
    submenu_2.append_item(function_item_2)
    submenu_2.append_item(item2)
    # Menu item for opening submenu 2
    submenu_item_2 = SubmenuItem("Another submenu", submenu=submenu_2)
    submenu_item_2.set_menu(menu)

    # Create a third submenu which uses double-line border
    submenu_3 = ConsoleMenu("Third Submenu", "This Time with Double-Line Borders.",
                            prologue_text="This is my prologue. I am currently showing my top and bottom borders, but \
they are hidden by default. Also notice that my text is really long, so it extends beyond a single line, and should \
wrap properly within the menu borders. This is a useful place to put instructions to the user about how to use \
the menu.",
                            epilogue_text="This is my epilogue. My borders are currently hidden.",
                            formatter=MenuFormatBuilder()
                            .set_title_align('center')
                            .set_subtitle_align('center')
                            .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER)
                            .show_prologue_top_border(True)
                            .show_prologue_bottom_border(True))
    submenu_3.append_item(function_item_2)
    submenu_3.append_item(MenuItem("Third Item. Does Nothing."))
    # Menu item for opening submenu 3
    submenu_item_3 = SubmenuItem("Third Submenu", submenu=submenu_3)
    submenu_item_3.set_menu(menu)

    # Add all the items to the root menu
    menu.append_item(item1)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)
    menu.append_item(submenu_item_2)
    menu.append_item(submenu_item_3)

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
