from typing import Optional

Operation = tuple[str, int | None]

class Node:

    def __init__(self, val: int, next_node: Optional["Node"] = None, prev_node: Optional["Node"] = None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node


class QueueList:

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def get(self) -> int | str:
        if self.size() == 0:
            return "error"
        old_tail = self.tail
        if not self.tail.prev_node:
            self.tail = None
        else:
            self.tail = self.tail.prev_node
        self._size -= 1
        return old_tail.val

    def put(self, val: int) -> None:
        new_node = Node(val, next_node=self.head, prev_node=None)
        if self.size() == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        self._size += 1


def read_input() -> list[Operation]:
    ops_num = input()
    ops = []
    for i in range(int(ops_num)):
        op = input()
        op_split = op.strip().split()
        if len(op_split) > 1:
            op_parsed = (op_split[0], int(op_split[1]))
            ops.append(op_parsed)
        else:
            ops.append((op_split[0], None))

    return ops


if __name__ == "__main__":
    ops = read_input()
    q = QueueList()
    for op in ops:
        if op[1] is None:
            print(getattr(q, op[0])())
        else:
            getattr(q, op[0])(op[1])
