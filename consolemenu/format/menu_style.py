from consolemenu.format.menu_borders import MenuBorderStyle, AsciiBorderStyle
from consolemenu.format.menu_margins import MenuMargins
from consolemenu.format.menu_padding import MenuPadding


class MenuStyle(object):
    """
    Class for specifying menu styling, such as margins, padding, and border style.
    """
    def __init__(self, margins=None, padding=None, border_style=AsciiBorderStyle()):
        if margins is None:
            margins = MenuMargins()
        if padding is None:
            padding = MenuPadding()
        if not isinstance(margins, MenuMargins):
            raise TypeError('margins must be of type MenuMargins')
        if not isinstance(padding, MenuPadding):
            raise TypeError('padding must be of type MenuPadding')
        if not isinstance(border_style, MenuBorderStyle):
            raise TypeError('border must be of type MenuBorderStyle')
        self.__margins = margins
        self.__padding = padding
        self.__border_style = border_style

    @property
    def margins(self): return self.__margins

    @margins.setter
    def margins(self, margins):
        if not isinstance(margins, MenuMargins):
            raise TypeError('margins must be of type MenuMargins')
        self.__margins = margins

    @property
    def padding(self): return self.__padding

    @padding.setter
    def padding(self, padding):
        if not isinstance(padding, MenuPadding):
            raise TypeError('padding must be of type MenuPadding')
        self.__padding = padding

    @property
    def border_style(self): return self.__border_style

    @border_style.setter
    def border_style(self, border_style):
        if not isinstance(border_style, MenuBorderStyle):
            raise TypeError('border_style must be of type MenuBorderStyle')
        self.__border_style = border_style
