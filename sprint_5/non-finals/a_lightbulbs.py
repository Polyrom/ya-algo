import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    brightest = float("-inf")
    rights = []
    while root or len(rights) > 0:
        while root:
            brightest = max(root.value, brightest)
            rights.append(root.right)
            root = root.left
        root = rights.pop()
    return int(brightest)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()
