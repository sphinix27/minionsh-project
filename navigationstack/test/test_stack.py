import unittest
from navigationstack.stack import Stack


class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_stack_is_empty_when_is_initialized(self):
        self.assertTrue(self.stack.is_empty())

    def test_stack_is_not_empty_after_adding_items(self):
        self.stack.push('item')
        self.assertFalse(self.stack.is_empty())

    def test_stack_pop_returns_the_last_item_added(self):
        expected = 'item'
        self.stack.push(expected)
        actual = self.stack.pop()
        self.assertEqual(expected, actual)
        self.assertTrue(self.stack.is_empty())


if __name__ == "__main__":
    unittest.main()
