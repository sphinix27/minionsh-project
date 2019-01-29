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
