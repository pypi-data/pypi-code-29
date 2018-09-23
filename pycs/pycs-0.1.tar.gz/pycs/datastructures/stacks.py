"""Implements a simple Stack datatype in python"""

class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def __str__(self):
        return str(self.val)


class Stack:
    def __init__(self, vals=None):
        self.top = None
        self.min = None
        self._len = 0

        if vals is not None:
            self.add_multiple(vals)

    def add_multiple(self, vals):
        for val in vals:
            self.add(val)

    def __iter__(self):
        curr = self.top
        while curr:
            yield curr
            curr = curr.next_node

    def __len__(self):
        return self._len

    def __str__(self):
        vals = [str(x) for x in self]
        return '->'.join(vals)

    def __repr__(self):
        return self.__str__()

    def add(self, val):
        if self.top is None:
            self.top = Node(val)
        else:
            node = Node(val)
            node.next_node = self.top
            self.top = node
        
        self._len += 1
        return self

    def pop(self):
        if self.top is None:
            return ValueError('Stack is empty')
        val = self.top.val
        self.top = self.top.next_node
        
        self._len -= 1
        return val

    def peek(self):
        return self.top.val

    def is_empty(self):
        return not self.top


def main():
    stack = Stack()
    stack.add_multiple([1,2,3,9, 74, 5, 0])
    return stack
if __name__ == '__main__':
    stack = main()

