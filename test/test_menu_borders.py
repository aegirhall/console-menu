from __future__ import print_function

from base_test_case import BaseTestCase
from consolemenu.format.menu_borders import AsciiBorderStyle, UnicodeLightBorderStyle


class TestAsciiMenuBorder(BaseTestCase):

    def test(self):
        border = AsciiBorderStyle()
        # print(border.bottom_left_corner)
        # print(border.bottom_right_corner)
        # print(border.top_left_corner)
        # print(border.top_right_corner)
        # print(border.outer_horizontal)
        # print(border.outer_horizontal_inner_down)
        # print(border.outer_horizontal_inner_up)
        # print(border.outer_vertical)
        # print(border.outer_vertical_inner_left)
        # print(border.outer_vertical_inner_right)

        self.assertEquals('+', border.bottom_left_corner)
        self.assertEquals('+', border.bottom_right_corner)
        self.assertEquals('+', border.top_left_corner)
        self.assertEquals('+', border.top_right_corner)
        self.assertEquals('-', border.outer_horizontal)
        self.assertEquals('+', border.outer_horizontal_inner_down)
        self.assertEquals('+', border.outer_horizontal_inner_up)
        self.assertEquals('|', border.outer_vertical)
        self.assertEquals('|', border.outer_vertical_inner_left)
        self.assertEquals('|', border.outer_vertical_inner_right)


class TestUnicodeLightMenuBorder(BaseTestCase):

    def test(self):
        border = UnicodeLightBorderStyle()
        # print border.bottom_left_corner
        # print border.bottom_right_corner
        # print border.top_left_corner
        # print border.top_right_corner
        # print border.outer_horizontal
        # print border.outer_horizontal_inner_down
        # print border.outer_horizontal_inner_up
        # print border.outer_vertical
        # print border.outer_vertical_inner_left
        # print border.outer_vertical_inner_right

        self.assertEquals(u'\u2514', border.bottom_left_corner)
        self.assertEquals(u'\u2518', border.bottom_right_corner)
        self.assertEquals(u'\u250C', border.top_left_corner)
        self.assertEquals(u'\u2510', border.top_right_corner)
        self.assertEquals(u'\u2500', border.outer_horizontal)
        self.assertEquals(u'\u252C', border.outer_horizontal_inner_down)
        self.assertEquals(u'\u2534', border.outer_horizontal_inner_up)
        self.assertEquals(u'\u2502', border.outer_vertical)
        self.assertEquals(u'\u2524', border.outer_vertical_inner_left)
        self.assertEquals(u'\u251C', border.outer_vertical_inner_right)
