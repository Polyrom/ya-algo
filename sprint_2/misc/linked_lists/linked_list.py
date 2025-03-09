from typing import Self


class Node:
    def __init__(self, val: int, nxt: Self | None):
        self.val = val
        self.next = nxt


def print_linked_list(vertex: Node):
    ll_elems = []
    while vertex:
        ll_elems.append(vertex.val)
        ll_elems.append(" -> ")
        vertex = vertex.next
    ll_elems.append(None)
    print("".join(map(str, ll_elems)))


if __name__ == "__main__":
    ll = Node(12, Node(4, Node(8, None)))
    print_linked_list(ll)
