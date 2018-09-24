from api import Cube
import sys

print("Model=" + sys.argv[1])
print("Embeddings=" + sys.argv[2])
print("Input file=" + sys.argv[3])
print("Output file=" + sys.argv[4])

from io_utils.cupt import CUPTDataset

dataset = CUPTDataset(file=sys.argv[3])

from io_utils.encodings import Encodings

encodings = Encodings()
encodings.load(sys.argv[1] + '.encodings')
from io_utils.embeddings import WordEmbeddings

embeddings = WordEmbeddings()
embeddings.read_from_file(sys.argv[2], None, False)

from generic_networks.ner import GDBNer
from io_utils.config import GDBConfig

config = GDBConfig()
ner = GDBNer(config, encodings, embeddings, runtime=True)
ner.load(sys.argv[1] + '.bestFScore')

f = open(sys.argv[4], "w")
f.write("# global.columns = ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC PARSEME:MWE\n")

for seq in dataset.sequences:
    item_list, label_list = ner.tag(seq)
    # print (item_list)
    # print (label_list)
    for entry in seq:
        entry.label = '*'
    index = 0
    for items, label in zip(item_list, label_list):
        index += 1
        suffix = ":" + label
        for item in items:
            final_label = str(index) + suffix
            if item != 0:
                if seq[item].label == '*':
                    seq[item].label = final_label
                    suffix = ""
                else:
                    seq[item].label += ';' + final_label

    for entry in seq[1:]:
        f.write(str(
            entry.index) + "\t" + entry.word + "\t" + entry.lemma + "\t" + entry.upos + "\t" + entry.xpos + "\t" + entry.attrs + "\t" + str(
            entry.head) + "\t" + "_" + "\t" + entry.deps + "\t" + "_" + "\t" + entry.label + "\n")
    f.write("\n")

f.close()
