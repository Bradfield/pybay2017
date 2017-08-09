

class Queue(object):
    """
    A slow but simple implementation of a first in, first out data structure.

    Don't do this in practice!
    """
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return self.size() == 0
