from pathlib import Path

from bytewax.dataflow import Dataflow
import bytewax.operators as op
from bytewax.connectors.stdio import StdOutSink
from bytewax.connectors.files import (
    DirSink,
    DirSource,
)

def to_tuple(x):
    return tuple(map(str, x.split(',')))

flow = Dataflow("k8s_cluster")
inp1 = op.input("inp", flow, DirSource(Path("./sample_data/cluster")))
inp2 = op.map("upper", inp1, str.upper)
out = op.map("tuple", inp2, to_tuple)
op.output("out1", out, DirSink(Path("./cluster_out/"), 2, assign_file=int))
op.output("out2", out, StdOutSink())


# import os
# from pathlib import Path

# from bytewax.dataflow import Dataflow
# from bytewax.connectors.stdio import StdOutput
# from bytewax.connectors.files import DirInput, DirOutput, FileInput, FileOutput

# input_dir = Path("./sample_data/cluster/")
# output_dir = Path("./cluster_out/")

# def to_tuple(x):
#     return tuple(map(str, x.split(',')))

# flow = Dataflow()
# flow.input("inp", DirInput(input_dir))
# flow.map(str.upper)
# flow.map(to_tuple)
# flow.output("out", DirOutput(output_dir, 5, assign_file=int))


# To run this example using helm you need to run the following
# helm upgrade --install k8s-cluster \
#   bytewax/bytewax \
#   --set configuration.pythonFileName=k8s_cluster.py \
#   --set configuration.processesCount=2 \
#   --set configuration.configMap.files.tarName=examples.tar \
#   --set configuration.keepAlive=true

# Also, you could use Waxctl to run the example. For that you can download it from https://bytewax.io/downloads
# And then, run these commands in your terminal to run a cluster of two containers:

# $ tar -C ./ -cvf cluster.tar examples
# $ waxctl dataflow deploy ./cluster.tar \
#     --name k8s-cluster \
#     --python-file-name examples/k8s_cluster.py \
#     -p2 --debug --keep-alive=true --yes

# Regardless of how you have executed the example (helm CLI or waxctl):

# Each worker will read the files in
# ./examples/sample_data/cluster/*.txt which have lines like
# `ONE1`.

# They will then both finish and you'll see ./cluster_out/part_0
# and ./cluster_out/part_1 with the data that each process in the
# cluster wrote with the lines uppercased.

# To see that files in each container you can run these commands:

# kubectl exec -it k8s-cluster-0 -cprocess -- cat /var/bytewax/cluster_out/part_0
# kubectl exec -it k8s-cluster-1 -cprocess -- cat /var/bytewax/cluster_out/part_1

# You could imagine reading from / writing to separate Kafka
# partitions, S3 blobs, etc.

