# ./simple.py
import bytewax.operators as op
from bytewax.testing import TestingSource
from bytewax.dataflow import Dataflow
from bytewax.connectors.stdio import StdOutSink

flow = Dataflow("simple")

out = op.input("inp1", flow, TestingSource(range(99999999)))
op.output("out", out, StdOutSink())
