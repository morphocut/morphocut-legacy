from leadeagle.processing.graph import NodeBase


class Sequential(NodeBase):
    """
    A sequence of individual processing nodes.
    """

    def __init__(self, sequence=None):
        self.sequence = sequence or []

    def append(self, node):
        self.sequence.append(node)

    def process(self, input=None):
        wp = input
        for n in self.sequence:
            wp = n.process(wp)

        return wp
