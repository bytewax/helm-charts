import json
import datetime as dt

from bytewax import Dataflow, cluster_main, parse
from bytewax.inputs import Emit, AdvanceTo, ManualInputConfig

def input_builder(worker_index, worker_count, resume_epoch):
    for epoch in range(100):
        yield AdvanceTo(epoch)
        yield Emit(epoch)

def output_builder(worker_index, worker_count):
    def output_handler(epoch_item):
        epoch, item = epoch_item
        print(f"worker: {worker_index} - epoch: {epoch} - item: {item}")
    return output_handler

flow = Dataflow()
flow.capture()

if __name__ == "__main__":
    cluster_main(
        flow, ManualInputConfig(input_builder), output_builder, **parse.proc_env()
    )