Operation = tuple[str, int | None]


class MyQueueSized:

    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.items = [None] * self.cap
        self.head = 0
        self.tail = 0
        self.q_size = 0

    def is_empty(self) -> None:
        return self.q_size == 0

    def size(self) -> None:
        print(self.q_size)

    def peek(self) -> None:
        print(self.items[self.head])

    def push(self, val: int) -> None:
        if self.q_size == self.cap:
            print("error")
            return
        self.items[self.tail] = val
        self.tail = (self.tail + 1) % self.cap
        self.q_size += 1

    def pop(self) -> None:
        if self.is_empty():
            print(None)
            return
        x = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.cap
        self.q_size -= 1
        print(x)


def read_input() -> tuple[int, list[Operation]]:
    ops_num = input()
    cap = input()
    ops = []
    for i in range(int(ops_num)):
        op = input()
        op_split = op.strip().split()
        if len(op_split) > 1:
            op_parsed = (op_split[0], int(op_split[1]))
            ops.append(op_parsed)
        else:
            ops.append((op_split[0], None))

    return int(cap), ops


if __name__ == "__main__":
    cap, ops = read_input()
    q = MyQueueSized(cap)
    for op in ops:
        if op[1] is None:
            getattr(q, op[0])()
        else:
            getattr(q, op[0])(op[1])


