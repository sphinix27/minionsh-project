from navigationstack.action import Action
from navigationstack.stack import Stack


class NavigationStack(Action):

    def __init__(self):
        self.redo_stack = Stack()
        self.undo_stack = Stack()

    def redo(self):
        if (self.can_redo()):
            item = self.undo_stack.pop()
            self.redo_stack.push(item)

    def undo(self):
        if (self.can_undo()):
            item = self.redo_stack.pop()
            self.undo_stack.push(item)

    def add(self, item):
        self.redo_stack.push(item)

    def can_undo(self):
        return not self.redo_stack.is_empty()

    def can_redo(self):
        return not self.undo_stack.is_empty()
