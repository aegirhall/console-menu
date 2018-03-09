
from base_test_case import BaseTestCase

from consolemenu import MultiSelectMenu
from consolemenu.items import FunctionItem


class TestMultiSelectMenu(BaseTestCase):

    def setUp(self):
        super(TestMultiSelectMenu, self).setUp()

        self.menu = MultiSelectMenu("Root Menu", "This is a Multi-Select Menu")
        self.menu.append_item(FunctionItem("Action Item 1", self.detect_action, args=['one']))
        self.menu.append_item(FunctionItem("Action Item 2", self.detect_action, args=['two']))
        self.menu.append_item(FunctionItem("Action Item 3", self.detect_action, args=['three']))
        self.menu.append_item(FunctionItem("Action Item 4", self.detect_action, args=['four']))

        self.action_detector = dict()
        self.assertIsNone(self.action_detector.get('one'))
        self.assertIsNone(self.action_detector.get('two'))
        self.assertIsNone(self.action_detector.get('three'))
        self.assertIsNone(self.action_detector.get('four'))

    def detect_action(self, action):
        self.action_detector[action] = True

    def test_1and2(self):
        self.mock_screen().input.return_value = '1,2,5'
        self.menu.start()
        self.menu.wait_for_start(10)
        self.menu.join(timeout=10)

        self.assertTrue(self.action_detector.get('one'))
        self.assertTrue(self.action_detector.get('two'))
        self.assertIsNone(self.action_detector.get('three'))
        self.assertIsNone(self.action_detector.get('four'))

    def test_1and3(self):
        self.mock_screen().input.return_value = '1,3,5'
        self.menu.start()
        self.menu.wait_for_start(10)
        self.menu.join(timeout=10)

        self.assertTrue(self.action_detector.get('one'))
        self.assertIsNone(self.action_detector.get('two'))
        self.assertTrue(self.action_detector.get('three'))
        self.assertIsNone(self.action_detector.get('four'))

    def test_1to3(self):
        self.mock_screen().input.return_value = '1-3,5'
        self.menu.start()
        self.menu.wait_for_start(10)
        self.menu.join(timeout=10)

        self.assertTrue(self.action_detector.get('one'))
        self.assertTrue(self.action_detector.get('two'))
        self.assertTrue(self.action_detector.get('three'))
        self.assertIsNone(self.action_detector.get('four'))

    def test_1to4(self):
        self.mock_screen().input.return_value = '1-4,5'
        self.menu.start()
        self.menu.wait_for_start(10)
        self.menu.join(timeout=10)

        self.assertTrue(self.action_detector.get('one'))
        self.assertTrue(self.action_detector.get('two'))
        self.assertTrue(self.action_detector.get('three'))
        self.assertTrue(self.action_detector.get('four'))

    def test_2and3(self):
        self.mock_screen().input.return_value = '2,3,5'
        self.menu.start()
        self.menu.wait_for_start(10)
        self.menu.join(timeout=10)

        self.assertIsNone(self.action_detector.get('one'))
        self.assertTrue(self.action_detector.get('two'))
        self.assertTrue(self.action_detector.get('three'))
        self.assertIsNone(self.action_detector.get('four'))

    def test_3to4(self):
        self.mock_screen().input.return_value = '3-4,5'
        self.menu.start()
        self.menu.wait_for_start(10)
        self.menu.join(timeout=10)

        self.assertIsNone(self.action_detector.get('one'))
        self.assertIsNone(self.action_detector.get('two'))
        self.assertTrue(self.action_detector.get('three'))
        self.assertTrue(self.action_detector.get('four'))

    def test_4to2(self):
        self.mock_screen().input.return_value = '4-2,5'
        self.menu.start()
        self.menu.wait_for_start(10)
        self.menu.join(timeout=10)

        self.assertIsNone(self.action_detector.get('one'))
        self.assertTrue(self.action_detector.get('two'))
        self.assertTrue(self.action_detector.get('three'))
        self.assertTrue(self.action_detector.get('four'))
