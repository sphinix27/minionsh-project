import unittest
from navigationstack.stack import Stack


class StackTest(unittest.TestCase):

    def test_stack_is_empty_when_is_initialized(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())


if __name__ == "__main__":
    unittest.main()
