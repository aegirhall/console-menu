
from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import PromptUtils

from colors import color

#
# Example 6 shows the use of colors in a ConsoleMenu.
# NOTE: This example requires the 'ansicolors' package to be installed: pip install ansicolors
#


def action(color_name):
    text = """
Dark spruce forest frowned on either side of the frozen waterway.
The trees had been stripped by a recent wind of their white covering of frost,
 and they seemed to lean toward each other, black and ominous, in the fading
light. A vast silence reigned over the land.
 """
    print(color(text, fg=color_name))
    PromptUtils(Screen()).enter_to_continue()


def main():

    # Create the root menu
    menu = ConsoleMenu("Color Menu", "This is a Console Menu with Colors")

    # Add all the items to the root menu
    menu.append_item(FunctionItem("Show {} text".format(color("Red", fg='red')), action, args=['red']))
    menu.append_item(FunctionItem("Show {} text".format(color("Blue", fg='blue')), action, args=['blue']))
    menu.append_item(FunctionItem("Show {} text".format(color("Yellow", fg='yellow')), action, args=['yellow']))
    menu.append_item(FunctionItem("Show {} text".format(color("Green", fg='green')), action, args=['green']))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
