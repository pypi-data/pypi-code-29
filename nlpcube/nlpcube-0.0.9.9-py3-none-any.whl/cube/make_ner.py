import sys
from api import Cube


# seqs = cube("This is a simple test.")
#
# for seq in seqs:
#     for entry in seq:
#         print (str(entry.index) + "\t" + str(entry.word) + "\t" + str(entry.lemma) + "\t" + str(
#             entry.upos) + "\t" + str(entry.xpos) + "\t" + str(entry.attrs) + "\t" + str(entry.head) + "\t" + str(
#             entry.label) + "\n")
#     print("\n")


def get_next_example(lines, pos):
    if pos >= len(lines):
        return None, -1
    seq = []
    from io_utils.conll import ConllEntry
    index = 1
    while pos < len(lines):
        if lines[pos].strip() == "":
            pos += 1
            break
        else:
            parts = lines[pos].split(" ")
            seq.append(ConllEntry(index, parts[0], "", "", "", "", 0, "", "", parts[3].strip()))
        pos += 1
        index += 1

    return seq, pos


def get_ner_type_and_index(entry, ner_index, ner_type):
    if entry.space_after != "O":
        parts = entry.space_after.split("-")
        # print (parts)
        new_ner_type = parts[1]

        if new_ner_type != ner_type or parts[0] == "B":
            ner_index += 1
            label = str(ner_index) + ":" + new_ner_type
        else:
            label = str(ner_index)
    else:
        # ner_type = "*"
        new_ner_type = "*"
        label = "*"

    return ner_index, new_ner_type, label


import sys

print ("input file is:" + sys.argv[1])
print ("output file is:" + sys.argv[2])

f = open(sys.argv[1], "r")
outf = open(sys.argv[2], "w")

lines = f.readlines()
from io_utils.conll import Dataset

ds = Dataset()

ds.sequences = []
pos = 2

print("Loading the Cube")
cube = Cube()
cube.load('en', tokenization=False)
print ("Done")
while True:
    seq, pos = get_next_example(lines, pos)
    if pos == -1:
        break
    seq = cube([seq])[0]
    ner_type = "*"
    ner_index = 0
    for entry in seq:
        ner_index, ner_type, mwe_label = get_ner_type_and_index(entry, ner_index, ner_type)
        outf.write(str(
            entry.index) + "\t" + entry.word + "\t" + entry.lemma + "\t" + entry.upos + "\t" + entry.xpos + "\t" + entry.attrs + "\t" + str(
            entry.head) + "\t" + entry.label + "\t" + entry.deps + "\t" + "_" + "\t" + mwe_label + "\n")

    outf.write("\n")
    outf.flush()

    ds.sequences.append(seq)

# ds.write(sys.argv[2])

f.close()
outf.close()
