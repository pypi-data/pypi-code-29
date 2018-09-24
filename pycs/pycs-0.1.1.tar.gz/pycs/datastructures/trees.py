class Node:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def add(self, value):
        if self.root is None:
            self.root = value
        else:
            ...


def main():
    ...


if __name__ == "__main__":
    main()
