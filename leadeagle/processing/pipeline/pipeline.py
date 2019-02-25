from leadeagle.processing.pipeline import NodeBase
from queue import Queue
from threading import Thread
from multiprocessing import cpu_count


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
        print('wp = ' + str(wp))
        for n in self.sequence:
            print('pipeline step: ' + str(n))
            wp = n(wp)
            print('wp = ' + str(wp))
        return wp

    def execute(self):
        for s in self():
            print('')


class MultiThreadPipeline(Pipeline):
    _sentinel = object()

    def __init__(self, sequence=None, num_workers=None):
        super().__init__(sequence=sequence)

        self.input_queue = Queue(maxsize=10)
        self.result_queue = Queue(maxsize=10)
        self.num_workers = cpu_count() if num_workers is None else num_workers

    def _fill_queue(self, iterator, queue):
        try:
            for x in iterator:
                queue.put(x)
        finally:
            queue.put(self._sentinel)

    def _process(self):
        input = self._yield_from_queue(self.input_queue)
        self._fill_queue(Pipeline.__call__(self, input), self.result_queue)

    def _yield_from_queue(self, queue):
        while True:
            x = queue.get()
            if x == self._sentinel:
                break
            yield x

    def __call__(self, input=None):
        fill_input = Thread(
            target=self._fill_queue,
            args=(input, self.input_queue),
            daemon=True)
        fill_input.start()

        for _ in range(self.num_workers):
            worker = Thread(
                target=self._process,
                daemon=True)
            worker.start()

        return self._yield_from_queue(self.result_queue)
