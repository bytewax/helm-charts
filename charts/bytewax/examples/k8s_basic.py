from bytewax.dataflow import Dataflow
from bytewax.connectors.stdio import StdOutput
from bytewax.inputs import StatelessSource, DynamicInput
import time

class NumberSource(StatelessSource):
    def __init__(self, max, worker_index):
        self.worker_index = worker_index
        self.iterator = iter(range(max))

    def next(self):
        time.sleep(1)
        return f"Worker: {self.worker_index} - {next(self.iterator)}"

    def close(self):
        pass


class NumberInput(DynamicInput):
    def __init__(self, max):
        self.max = max

    def build(self, worker_index, worker_count):
        return NumberSource(self.max, worker_index)


flow = Dataflow()
flow.input("inp", NumberInput(100))
flow.output("out", StdOutput())