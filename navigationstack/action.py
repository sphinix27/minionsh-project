import abc


class Action(abc.ABC):
    @abc.abstractmethod
    def redo(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass
