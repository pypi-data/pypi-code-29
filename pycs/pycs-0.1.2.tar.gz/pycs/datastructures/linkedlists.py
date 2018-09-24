#!/usr/bin/env python

from random import randint


class Node(object):
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.val)


class LinkedList(object):
    def __init__(self, vals=None):
        self.head = None
        self.tail = None

        if vals is not None:
            self.add_multiple(vals)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next_node

    def __str__(self):
        vals = [str(x) for x in self]
        return "->".join(vals)

    def __repr__(self):
        vals = [str(x) for x in self]
        return "->".join(vals)

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next_node

        return length

    def add(self, val):
        if self.head is None:
            self.tail = self.head = Node(val)
        else:
            self.tail.next_node = Node(val)
            self.tail = self.tail.next_node
        return self.tail

    def add_left(self, val):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            self.head = Node(val, next_node=self.head)
        return self.head

    def add_multiple(self, vals):
        for val in vals:
            self.add(val)

    def pop(self):
        if self.tail is None:
            raise ValueError("List is empty")

        curr = self.head
        # Check for case that list has only one element
        if self.head == self.tail:
            val = self.head.val
            self.head = self.tail = None
            return val

        while curr:
            if curr.next_node == self.tail:
                val = self.tail.val
                self.tail = curr
                self.tail.next_node = None
                return val
            curr = curr.next_node

    def pop_left(self):
        if self.head is None:
            raise ValueError("List is empty")

        val = self.head.val
        self.head = self.head.next_node

        return val

    def generate(self, n=10, min_val=0, max_val=100):
        for i in range(n):
            number = randint(min_val, max_val)
            self.add(number)

        return self


def main():
    l = LinkedList()
    l.generate(n=5)
    print(l)
    print(len(l))


if __name__ == "__main__":
    main()
