
from consolemenu import *
from consolemenu.items import *

#
# Example 3 shows the use of a multi-select menu. A multi-select menu will execute all of the
# selected actions with a single user input prompt.
#


def action(name):
    print("\nHello from action {}!!!\n".format(name))
    Screen().input('Press [Enter] to continue')


def main():

    # Create the root menu
    menu = MultiSelectMenu("Root Menu", "This is a Multi-Select Menu",
                           epilogue_text=("Please select one or more entries separated by commas, and/or a range "
                                          "of numbers. For example:  1,2,3   or   1-4   or   1,3-4"),
                           exit_option_text='Exit Application')  # Customize the exit text

    # Add all the items to the root menu
    menu.append_item(FunctionItem("Action Item 1", action, args=['one']))
    menu.append_item(FunctionItem("Action Item 2", action, args=['two']))
    menu.append_item(FunctionItem("Action Item 3", action, args=['three']))
    menu.append_item(FunctionItem("Action Item 4", action, args=['four']))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
