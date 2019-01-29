class Stack(object):

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
