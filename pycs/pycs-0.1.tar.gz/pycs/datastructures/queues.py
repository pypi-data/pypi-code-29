

class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def __str__(self):
        return str(self.val)
    
class Queue:
    def __init__(self, vals=None):
        self.first = None
        self.last = None
    
        if vals is not None:
            self.add_multiple(vals)

    def __iter__(self):
        curr = self.first
        while curr:
            yield curr
            curr = curr.next_node

    def __len__(self):
        length = 0
        curr = self.first
        while curr:
            length += 1
            curr = curr.next_node

        return length

    def __str__(self):
        vals = [str(x) for x in self]
        return '->'.join(vals)

    def __repr__(self):
        return self.__str__()

    def add(self, val):
        if self.last is None:
            self.first = self.last = Node(val)
        else:
            node = Node(val)
            self.last.next_node = node
            self.last = node

        return self

    def add_multiple(self, vals):
        for val in vals:
            self.add(val)
        return self

    def remove(self):
        val = self.first.val
        self.first = self.first.next_node

        return val

    def peek_first(self):
        return self.first.val

    def peek_last(self):
        return self.last.val


def main():
    queue = Queue()

    return queue


if __name__ == '__main__':
    queue = main()

