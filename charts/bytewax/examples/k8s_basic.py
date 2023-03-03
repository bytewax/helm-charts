from bytewax.dataflow import Dataflow
from bytewax.execution import cluster_main
from bytewax.inputs import ManualInputConfig
from bytewax.outputs import ManualOutputConfig
from bytewax import parse
import time

def input_builder(worker_index, worker_count, resume_epoch):
    # Ignore state recovery here
    state = None
    for i in range(100):
        time.sleep(1)
        yield state, i

def output_builder(worker_index, worker_count):
    def output_handler(item):
        print(f"worker: {worker_index} - item: {item}")
    return output_handler

flow = Dataflow()
flow.input("inp", ManualInputConfig(input_builder))
flow.capture(ManualOutputConfig(output_builder))

if __name__ == "__main__":
    cluster_main(flow, **parse.proc_env())