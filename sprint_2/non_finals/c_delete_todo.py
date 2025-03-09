import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_node_by_index(head, idx):
    while idx:
        if not head.next_item:
            return None
        head = head.next_item
        idx -= 1
    return head


def solution(node, idx):
    if idx == 0:
        return node.next_item
    prev_node = get_node_by_index(node, idx-1)
    if not prev_node or not prev_node.next_item:
        return node
    prev_node.next_item = prev_node.next_item.next_item
    return node



def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == "__main__":
    test()
