from abc import abstractmethod, ABC

__all__ = ["NodeBase"]


class NodeBase(ABC):
    @abstractmethod
    def process(self, input=None):
        """
        Process the input stream
        """
        while False:
            yield None
