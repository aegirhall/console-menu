from consolemenu.format.menu_borders import MenuBorderStyle, MenuBorderStyleFactory
from consolemenu.format.menu_margins import MenuMargins
from consolemenu.format.menu_padding import MenuPadding


class MenuStyle(object):
    """
    Class for specifying menu styling, such as margins, padding, and border style.
    """

    def __init__(self, margins=None, padding=None, border_style=None, border_style_type=None,
                 border_style_factory=None):
        self.__margins = None
        self.__padding = None
        self.__border_style_factory = None
        self.__border_style = None

        if margins is None:
            margins = MenuMargins()
        self.margins = margins

        if padding is None:
            padding = MenuPadding()
        self.padding = padding

        if border_style_factory is None:
            border_style_factory = MenuBorderStyleFactory()
        self.border_style_factory = border_style_factory

        if border_style is not None:
            #  A specified border_style takes precedence
            self.border_style = border_style
        elif border_style_type is not None:
            # If we have a border style type, create border style with factory
            self.border_style = self.border_style_factory.create_border(border_style_type)
        else:
            # No border style class or type was given, so use default border style
            self.border_style = self.border_style_factory.create_light_border()

    @property
    def margins(self):
        return self.__margins

    @margins.setter
    def margins(self, margins):
        if not isinstance(margins, MenuMargins):
            raise TypeError('margins must be of type MenuMargins')
        self.__margins = margins

    @property
    def padding(self):
        return self.__padding

    @padding.setter
    def padding(self, padding):
        if not isinstance(padding, MenuPadding):
            raise TypeError('padding must be of type MenuPadding')
        self.__padding = padding

    @property
    def border_style(self):
        return self.__border_style

    @border_style.setter
    def border_style(self, border_style):
        if not isinstance(border_style, MenuBorderStyle):
            raise TypeError('border_style must be of type MenuBorderStyle')
        self.__border_style = border_style

    @property
    def border_style_factory(self):
        return self.__border_style_factory

    @border_style_factory.setter
    def border_style_factory(self, border_style_factory):
        if not isinstance(border_style_factory, MenuBorderStyleFactory):
            raise TypeError('border_style_factory must be of type MenuBorderStyleFactory')
        self.__border_style_factory = border_style_factory
