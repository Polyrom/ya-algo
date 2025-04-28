from typing import Optional
import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def remove(root, key) -> Optional[Node]:
    if not root:
        return None
    node, node_parent = root, None
    while node and node.value != key:
        node_parent = node
        node = node.left if node.value >= key else node.right
    if not node:
        return root
    if not node.left or not node.right:
        tmp = node.left if node.left else node.right
        if not node_parent:
            node = None
            return tmp
        if node == node_parent.left:
            node_parent.left = tmp
        else:
            node_parent.right = tmp
        node = None
    else:
        replacer_parent = node
        replacer = node.left
        while replacer.right:
            replacer_parent = replacer
            replacer = replacer.right
        node.value = replacer.value
        if replacer_parent == node:
            replacer_parent.left = replacer.left
        else:
            replacer_parent.right = replacer.left
        replacer = None
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == "__main__":
    test()
