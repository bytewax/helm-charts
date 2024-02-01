import bytewax.operators as op
from bytewax.testing import TestingSource
from bytewax.dataflow import Dataflow
from bytewax.connectors.stdio import StdOutSink
from bytewax.inputs import (
    DynamicSource,
    StatelessSourcePartition,
)
import time

class NumberSource(StatelessSourcePartition):
    def __init__(self, max, worker_index):
        self.worker_index = worker_index
        self.iterator = iter(range(max))

    def next_batch(self, worker_index):
        time.sleep(1)
        return [f"Worker: {self.worker_index} - {next(self.iterator)}"]

    def close(self):
        pass

class NumberInput(DynamicSource):
    def __init__(self, max):
        self.max = max

    def build(self, _now, worker_index, worker_count):
        return NumberSource(max=self.max, worker_index=worker_index)

flow = Dataflow("k8s_basic")
out = op.input("inp1", flow, NumberInput(100))
op.output("out", out, StdOutSink())
