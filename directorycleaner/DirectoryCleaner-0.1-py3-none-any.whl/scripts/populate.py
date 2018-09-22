#Short script to populate a directory with a bunch of empty files to simulate a messy directory.
#Could be modified to actually fill the files with random data to be more realistic.
import sys
import os

FILE_TYPES = (".txt", ".jpg", ".png", ".gif", ".js", ".py", ".php", ".rar", ".rtf")

def main(path, num):
    if os.path.isdir(path):
        for i, type in enumerate(FILE_TYPES):
            populate(path, num, type)


def populate(path, num, type):
    num = int(num)
    for i in range(num):
        file_name = "test" + str(i) + type
        file_name = os.path.join(path, file_name)
        with open(file_name, "w") as f:
            pass


if __name__ == "__main__":
    if sys.argv[1] and sys.argv[2]:
        main(sys.argv[1], sys.argv[2])
