# ./simple.py
from bytewax.dataflow import Dataflow
from bytewax.testing import TestingInput
from bytewax.connectors.stdio import StdOutput
import time

def slow_inc(x):
    time.sleep(5)
    return x + 1

flow = Dataflow()
flow.input("inp", TestingInput(range(99999999)))
flow.map(slow_inc)
flow.output("out", StdOutput())
