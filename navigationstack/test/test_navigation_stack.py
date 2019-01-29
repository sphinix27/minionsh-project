import unittest
from navigationstack.navigation_stack import NavigationStack


class TestNavigationStack(unittest.TestCase):

    def setUp(self):
        self.navigation_stack = NavigationStack()

    def test_navigation_stack_undo_and_redo_stacks_are_empty_when_initialized(self):
        self.assertTrue(self.navigation_stack.redo_stack.is_empty())
        self.assertTrue(self.navigation_stack.undo_stack.is_empty())

    def test_navigation_stack_add_items(self):
        self.navigation_stack.add('item')
        self.assertFalse(self.navigation_stack.redo_stack.is_empty())
        self.assertTrue(self.navigation_stack.undo_stack.is_empty())


if __name__ == "__main__":
    unittest.main()
