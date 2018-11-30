"""
Input nodes
"""

from leadeagle.processing.graph import NodeBase


class LocalDirectoryInput(NodeBase):
    """
    Source node (no predecessors).
    """

    def __init__(self, location):
        self.location = location

    def process(self, input=None):
        """
        Read the contents of a local directory and yield processing objects
        """
        while False:
            yield None
