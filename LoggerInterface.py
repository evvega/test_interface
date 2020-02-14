import abc


class ImplementLogger(abc.ABC):

    @abc.abstractmethod
    def log(self, msg: str): pass
