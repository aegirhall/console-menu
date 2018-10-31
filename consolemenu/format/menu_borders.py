import logging
import sys


class MenuBorderStyle(object):
    """
    Base class for console menu border. Each propery should be overridden by a subclass.
    """

    @property
    def bottom_left_corner(self): raise NotImplementedError()

    @property
    def bottom_right_corner(self): raise NotImplementedError()

    @property
    def inner_horizontal(self): raise NotImplementedError()

    @property
    def inner_vertical(self): raise NotImplementedError()

    @property
    def intersection(self): raise NotImplementedError()

    @property
    def outer_horizontal(self): raise NotImplementedError()

    @property
    def outer_horizontal_inner_down(self): raise NotImplementedError()

    @property
    def outer_horizontal_inner_up(self): raise NotImplementedError()

    @property
    def outer_vertical(self): raise NotImplementedError()

    @property
    def outer_vertical_inner_left(self): raise NotImplementedError()

    @property
    def outer_vertical_inner_right(self): raise NotImplementedError()

    @property
    def top_left_corner(self): raise NotImplementedError()

    @property
    def top_right_corner(self): raise NotImplementedError()


class AsciiBorderStyle(MenuBorderStyle):

    @property
    def bottom_left_corner(self): return '+'

    @property
    def bottom_right_corner(self): return '+'

    @property
    def inner_horizontal(self): return '-'

    @property
    def inner_vertical(self): return '|'

    @property
    def intersection(self): return '+'

    @property
    def outer_horizontal(self): return '-'

    @property
    def outer_horizontal_inner_down(self): return '+'

    @property
    def outer_horizontal_inner_up(self): return '+'

    @property
    def outer_vertical(self): return '|'

    @property
    def outer_vertical_inner_left(self): return '|'

    @property
    def outer_vertical_inner_right(self): return '|'

    @property
    def top_left_corner(self): return '+'

    @property
    def top_right_corner(self): return '+'


class LightBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using Unicode "light" box drawing characters.
    """

    @property
    def bottom_left_corner(self): return u'\u2514'

    @property
    def bottom_right_corner(self): return u'\u2518'

    @property
    def inner_horizontal(self): return u'\u2500'

    @property
    def inner_vertical(self): return u'\u2502'

    @property
    def intersection(self): return u'\u253C'

    @property
    def outer_horizontal(self): return u'\u2500'

    @property
    def outer_horizontal_inner_down(self): return u'\u252C'

    @property
    def outer_horizontal_inner_up(self): return u'\u2534'

    @property
    def outer_vertical(self): return u'\u2502'

    @property
    def outer_vertical_inner_left(self): return u'\u2524'

    @property
    def outer_vertical_inner_right(self): return u'\u251C'

    @property
    def top_left_corner(self): return u'\u250C'

    @property
    def top_right_corner(self): return u'\u2510'


class HeavyBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using Unicode "heavy" box drawing characters.
    """

    @property
    def bottom_left_corner(self): return u'\u2517'

    @property
    def bottom_right_corner(self): return u'\u251B'

    @property
    def inner_horizontal(self): return u'\u2501'

    @property
    def inner_vertical(self): return u'\u2503'

    @property
    def intersection(self): return u'\u254B'

    @property
    def outer_horizontal(self): return u'\u2501'

    @property
    def outer_horizontal_inner_down(self): return u'\u2533'

    @property
    def outer_horizontal_inner_up(self): return u'\u253B'

    @property
    def outer_vertical(self): return u'\u2503'

    @property
    def outer_vertical_inner_left(self): return u'\u252B'

    @property
    def outer_vertical_inner_right(self): return u'\u2523'

    @property
    def top_left_corner(self): return u'\u250F'

    @property
    def top_right_corner(self): return u'\u2513'


class HeavyOuterLightInnerBorderStyle(HeavyBorderStyle):
    """
    MenuBorderStyle class using Unicode "heavy" box drawing characters for the outer borders, and
    "light" box drawing characters for the inner borders.
    """

    @property
    def inner_horizontal(self): return u'\u2500'

    @property
    def inner_vertical(self): return u'\u2502'

    @property
    def intersection(self): return u'\u253C'

    @property
    def outer_horizontal_inner_down(self): return u'\u252F'

    @property
    def outer_horizontal_inner_up(self): return u'\u2537'

    @property
    def outer_vertical_inner_left(self): return u'\u2528'

    @property
    def outer_vertical_inner_right(self): return u'\u2520'


class DoubleLineBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using "double-line" box drawing characters.
    """

    @property
    def bottom_left_corner(self): return u'\u255A'

    @property
    def bottom_right_corner(self): return u'\u255D'

    @property
    def inner_horizontal(self): return u'\u2550'

    @property
    def inner_vertical(self): return u'\u2551'

    @property
    def intersection(self): return u'\u256C'

    @property
    def outer_horizontal(self): return u'\u2550'

    @property
    def outer_horizontal_inner_down(self): return u'\u2566'

    @property
    def outer_horizontal_inner_up(self): return u'\u2569'

    @property
    def outer_vertical(self): return u'\u2551'

    @property
    def outer_vertical_inner_left(self): return u'\u2563'

    @property
    def outer_vertical_inner_right(self): return u'\u2560'

    @property
    def top_left_corner(self): return u'\u2554'

    @property
    def top_right_corner(self): return u'\u2557'


class DoubleLineOuterLightInnerBorderStyle(DoubleLineBorderStyle):
    """
    MenuBorderStyle class using Unicode "double-line" box drawing characters for the outer borders, and
    "light" box drawing characters for the inner borders.
    """

    @property
    def inner_horizontal(self): return u'\u2500'

    @property
    def inner_vertical(self): return u'\u2502'

    @property
    def intersection(self): return u'\u253C'

    @property
    def outer_horizontal_inner_down(self): return u'\u2564'

    @property
    def outer_horizontal_inner_up(self): return u'\u2567'

    @property
    def outer_vertical_inner_left(self): return u'\u2562'

    @property
    def outer_vertical_inner_right(self): return u'\u255F'


class MenuBorderStyleType(object):
    """
    Defines the various menu border styles, as expected by the border factory.
    """
    ASCII_BORDER = 0
    """ Menu Border using pure ASCII characters. Usable on all platforms. """

    LIGHT_BORDER = 1
    """ Menu Border using the "light" box drawing characters. Should be usable on all platforms. """

    HEAVY_BORDER = 2
    """ Menu Border using the "heavy" box drawing characters.  NOTE: On Windows, this border style will work
        ONLY on Python 3.6.  It will raise a UnicodeEncodeError exception on earlier Python versions.
        If requesting this border style via the MenuBorderStyleFactory when on Windows/Python 3.5 or earlier, this
        border style will be substituted by the `DOUBLE_LINE_BORDER`. """

    DOUBLE_LINE_BORDER = 3
    """ Menu Border using "double-line" box drawing characters. """

    HEAVY_OUTER_LIGHT_INNER_BORDER = 4
    """ Menu Border using the "heavy" box drawing characters for the outer border elements, and "light" box-drawing
        characters for the inner border elements.
        NOTE: On Windows, this border style will work ONLY on Python 3.6.  It will raise a UnicodeEncodeError
        exception on earlier Python versions. If requesting this border style via the MenuBorderStyleFactory when
        on Windows/Python 3.5 or earlier, this border style will be substituted by the `DOUBLE_LINE_BORDER`. """

    DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER = 5
    """ Menu Border using the "double-line" box drawing characters for the outer border elements, and "light"
        box-drawing characters for the inner border elements."""


class MenuBorderStyleFactory(object):
    """
    Factory class for creating  MenuBorderStyle instances.
    """

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def create_border(self, border_style_type):
        """
        Create a new MenuBorderStyle instance based on the given border style type.
        :param border_style_type: an integer value from MenuBorderStyleType.
        :return: a new MenuBorderStyle instance.
        """
        if border_style_type == MenuBorderStyleType.ASCII_BORDER:
            return self.create_ascii_border()
        elif border_style_type == MenuBorderStyleType.LIGHT_BORDER:
            return self.create_light_border()
        elif border_style_type == MenuBorderStyleType.HEAVY_BORDER:
            return self.create_heavy_border()
        elif border_style_type == MenuBorderStyleType.DOUBLE_LINE_BORDER:
            return self.create_doubleline_border()
        elif border_style_type == MenuBorderStyleType.HEAVY_OUTER_LIGHT_INNER_BORDER:
            return self.create_heavy_outer_light_inner_border()
        elif border_style_type == MenuBorderStyleType.DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER:
            return self.create_doubleline_outer_light_inner_border()
        else:
            # Use ASCII if we don't recognize the type
            self.logger.info('Unrecognized border style type: {}. Defaulting to ASCII.'.format(border_style_type))
            return self.create_ascii_border()

    def create_ascii_border(self):
        """
        Create an ASCII border style.
        :return: a new instance of AsciiBorderStyle.
        """
        return AsciiBorderStyle()

    def create_light_border(self):
        """
        Create a border style using "light" box drawing characters.
        :return: a new instance of LightBorderStyle
        """
        return LightBorderStyle()

    def create_heavy_border(self):
        """
        Create a border style using "heavy" box drawing characters.
        NOTE: The Heavy border style will work on Windows ONLY when using Python 3.6. If on Windows and
        using an earlier version of Python, the heavy border will be substituted with the DOUBLE_LINE_BORDER.
        :return: a new instance of HeavyBorderStyle, unless on Windows and pre-Python 3.5 in which case a
                 new instance of DoubleLineBorderStyle will be returned.
        """
        # Special case for Windows...
        if self.is_win_python35_or_earlier():
            return DoubleLineBorderStyle()
        # All other platforms...
        return HeavyBorderStyle()

    def create_heavy_outer_light_inner_border(self):
        """
        Create a border style using "heavy" box drawing characters for outer border elements, and "light"
        box drawing characters for inner border elements.
        NOTE: The Heavy border style will work on Windows ONLY when using Python 3.6. If on Windows and
        using an earlier version of Python, the heavy border will be substituted with the DOUBLE_LINE_BORDER.
        :return: a new instance of HeavyBorderStyle, unless on Windows and pre-Python 3.5 in which case a
                 new instance of DoubleLineBorderStyle will be returned.
        """
        # Special case for Windows...
        if self.is_win_python35_or_earlier():
            return DoubleLineOuterLightInnerBorderStyle()
        # All other platforms...
        return HeavyOuterLightInnerBorderStyle()

    def create_doubleline_border(self):
        """
        Create a border style using "double-line" box drawing characters.
        :return: a new instance of DoubleLineBorderStyle.
        """
        return DoubleLineBorderStyle()

    def create_doubleline_outer_light_inner_border(self):
        """
        Create a border style using "double-line" box drawing characters for outer border elements, and "light"
        box drawing characters for inner border elements.
        :return: a new instance of DoubleLineOuterLightInnerBorderStyle
        """
        return DoubleLineOuterLightInnerBorderStyle()

    @staticmethod
    def is_win_python35_or_earlier():
        """ Convenience method to determine if the current platform is Windows and Python version 3.5 or earlier. """
        return sys.platform.startswith("win") and sys.version_info.major < 3 or (
                    sys.version_info.major == 3 and sys.version_info.minor < 6)
