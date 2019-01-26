from abc import abstractmethod, ABC

__all__ = ["NodeBase"]


class NodeBase(ABC):
    @abstractmethod
    def __call__(self, input=None):
        """
        Process the input stream
        """
        while False:
            yield None
