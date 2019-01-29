from navigationstack.stack import Stack
from navigationstack.action import Action


class NavigationStack(Action):

    def __init__(self):
        self.redo_stack = Stack()
        self.undo_stack = Stack()

    def redo(self):
        pass

    def undo(self):
        pass

    def add(self, item):
        self.redo_stack.push(item)

    def can_undo(self):
        return not self.redo_stack.is_empty()

    def can_redo(self):
        return False
