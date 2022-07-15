from collections import deque

from py_ds.data import Node


class SimpleLL:
    def __init__(self) -> None:
        self.head = None

    def append(self, node: Node) -> None:
        print(node.data)

    def __str__(self):
        pass


if __name__ == "__main__":
    node = Node()
    node.data = "erez"
    ll = SimpleLL()
    ll.append(node)
