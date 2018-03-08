from base_test_case import BaseTestCase
from consolemenu.format import *


class DummyMenuBorderStyle(LightBorderStyle):
    """ Dummy class to use for testing border style overrides in MenuStyle. """


class DummyMenuBorderStyleFactory(MenuBorderStyleFactory):
    """ Dummy class to use for testing menu border overrides in MenuStyle. """
    def create_border(self, border_style_type):
        if border_style_type == 8:
            return DummyMenuBorderStyle()
        else:
            return super(DummyMenuBorderStyleFactory, self).create_border(border_style_type)


class TestMenuStyle(BaseTestCase):

    def test_defaults(self):
        ms = MenuStyle()
        # Default Border Factory should be MenuBorderStyleFactory
        self.assertTrue(isinstance(ms.border_style_factory, MenuBorderStyleFactory))
        # Default Border style should be LightBorderStyle
        self.assertTrue(isinstance(ms.border_style, LightBorderStyle))
        # Default Margins
        self.assertTrue(isinstance(ms.margins, MenuMargins))
        self.assertEqual(1, ms.margins.top)
        self.assertEqual(2, ms.margins.left)
        self.assertEqual(0, ms.margins.bottom)
        self.assertEqual(2, ms.margins.right)
        # Default Padding
        self.assertTrue(isinstance(ms.padding, MenuPadding))
        self.assertEqual(1, ms.padding.top)
        self.assertEqual(2, ms.padding.left)
        self.assertEqual(1, ms.padding.bottom)
        self.assertEqual(2, ms.padding.right)

    def test_constructor_margins_and_padding(self):
        ms = MenuStyle(margins=MenuMargins(8, 7, 6, 5), padding=MenuPadding(12, 11, 10, 9))
        # Default Border Factory should be MenuBorderStyleFactory
        self.assertTrue(isinstance(ms.border_style_factory, MenuBorderStyleFactory))
        # Default Border style should be LightBorderStyle
        self.assertTrue(isinstance(ms.border_style, LightBorderStyle))
        # Given Margins
        self.assertTrue(isinstance(ms.margins, MenuMargins))
        self.assertEqual(8, ms.margins.top)
        self.assertEqual(7, ms.margins.left)
        self.assertEqual(6, ms.margins.bottom)
        self.assertEqual(5, ms.margins.right)
        # Given Padding
        self.assertTrue(isinstance(ms.padding, MenuPadding))
        self.assertEqual(12, ms.padding.top)
        self.assertEqual(11, ms.padding.left)
        self.assertEqual(10, ms.padding.bottom)
        self.assertEqual(9, ms.padding.right)

    def test_constructor_border_style_only(self):
        ms = MenuStyle(border_style=HeavyBorderStyle())
        self.assertTrue(isinstance(ms.border_style, HeavyBorderStyle))
        self.assertTrue(isinstance(ms.border_style_factory, MenuBorderStyleFactory))

    def test_constructor_border_style_type_only(self):
        ms = MenuStyle(border_style_type=MenuBorderStyleType.DOUBLE_LINE_BORDER)
        self.assertTrue(isinstance(ms.border_style, DoubleLineBorderStyle))
        self.assertTrue(isinstance(ms.border_style_factory, MenuBorderStyleFactory))

    def test_constructor_border_factory_only(self):
        ms = MenuStyle(border_style_factory=DummyMenuBorderStyleFactory())
        self.assertTrue(isinstance(ms.border_style, LightBorderStyle))
        self.assertTrue(isinstance(ms.border_style_factory, DummyMenuBorderStyleFactory))

    def test_constructor_conflicting_border_class_and_type(self):
        ms = MenuStyle(border_style=HeavyBorderStyle(), border_style_type=MenuBorderStyleType.LIGHT_BORDER)
        # Class should take precedence
        self.assertTrue(isinstance(ms.border_style, HeavyBorderStyle))
        self.assertTrue(isinstance(ms.border_style_factory, MenuBorderStyleFactory))

    def test_constructor_conflicting_border_factory_and_type(self):
        ms = MenuStyle(border_style_factory=DummyMenuBorderStyleFactory(), border_style_type=8)
        self.assertTrue(isinstance(ms.border_style, DummyMenuBorderStyle))
        self.assertTrue(isinstance(ms.border_style_factory, DummyMenuBorderStyleFactory))
