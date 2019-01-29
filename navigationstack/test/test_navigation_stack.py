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

    def test_navigation_stack_can_undo_and_can_redo_when_stacks_are_empty(self):
        self.assertFalse(self.navigation_stack.can_undo())
        self.assertFalse(self.navigation_stack.can_redo())

    def test_navigation_stack_can_undo_when_adding_items(self):
        self.navigation_stack.add('item')
        self.assertTrue(self.navigation_stack.can_undo())
        self.assertFalse(self.navigation_stack.can_redo())

    def test_navigation_stack_can_redo_when_undo_stack_is_not_empty(self):
        self.navigation_stack.add('item1')
        self.navigation_stack.add('item2')
        self.navigation_stack.undo()
        self.assertTrue(self.navigation_stack.can_undo())
        self.assertTrue(self.navigation_stack.can_redo())
        self.assertFalse(self.navigation_stack.redo_stack.is_empty())
        self.assertFalse(self.navigation_stack.undo_stack.is_empty())

    def test_navigation_stack_redo_when_is_not_empty(self):
        self.navigation_stack.add('item1')
        self.navigation_stack.add('item2')
        self.navigation_stack.add('item3')
        self.navigation_stack.undo()
        self.navigation_stack.undo()
        self.navigation_stack.redo()
        self.assertTrue(self.navigation_stack.can_undo())
        self.assertTrue(self.navigation_stack.can_redo())
        self.assertFalse(self.navigation_stack.redo_stack.is_empty())
        self.assertFalse(self.navigation_stack.undo_stack.is_empty())


if __name__ == "__main__":
    unittest.main()
