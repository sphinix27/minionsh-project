import abc


class Action(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def redo(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass
