class MenuPadding(object):
    """
    Class for menu padding. Padding is the area between the menu border and the content.
    """

    def __init__(self, top=1, left=2, bottom=1, right=2):
        self.__left = left
        self.__right = right
        self.__top = top
        self.__bottom = bottom

    @property
    def left(self): return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self): return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def top(self): return self.__top

    @top.setter
    def top(self, top):
        self.__top = top

    @property
    def bottom(self): return self.__bottom

    @bottom.setter
    def bottom(self, bottom):
        self.__bottom = bottom
