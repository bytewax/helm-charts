import collections

import tiny_dancer
from nltk.tokenize import RegexpTokenizer


def file_input():
    with open("pyexamples/sample_data/wordcount.txt") as lines:
        for line in lines:
            yield (1, line)


def tokenize(x):
    tokenizer = RegexpTokenizer(r"\w+")
    return tokenizer.tokenize(x)


def word_count(acc, words):
    for word in words:
        acc[word] += 1
    return acc


ec = tiny_dancer.Executor()
flow = ec.Dataflow(file_input())
flow.flat_map(tokenize)
flow.filter(lambda x: x != "and")
flow.exchange(hash)
flow.accumulate(lambda: collections.defaultdict(int), word_count)
flow.flat_map(dict.items)
flow.inspect(print)


if __name__ == "__main__":
    ec.build_and_run()
