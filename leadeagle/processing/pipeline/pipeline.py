from leadeagle.processing.pipeline import NodeBase


class Pipeline(NodeBase):
    """
    A sequence of individual processing nodes.
    """

    def __init__(self, sequence=None):
        self.sequence = sequence or []

    def append(self, node):
        self.sequence.append(node)

    def __call__(self, input=None):
        wp = input
        for n in self.sequence:
            wp = n(wp)

        return wp
