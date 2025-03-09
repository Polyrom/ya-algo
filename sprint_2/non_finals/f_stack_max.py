class Stack:
    def __init__(self) -> None:
        self.items: list[int] = []

    def size(self) -> int:
        return len(self.items)

    def pop(self) -> None:
        if self.size() == 0:
            print("error")
            return
        self.items.pop()

    def push(self, value) -> None:
        self.items.append(value)

    def get_max(self) -> None:
        if self.size() == 0:
            print("None")
            return
        mx = float("-inf")
        for value in self.items:
            if value > mx:
                mx = value
        print(mx)


def read_input() -> list[tuple[str, int | None]]:
    ops = []
    inputs_num = input()
    for _ in range(int(inputs_num)):
        op_raw = input()
        op_split = op_raw.split()
        if len(op_split) > 1:
            ops.append((op_split[0], int(op_split[1])))
        else:
            ops.append((op_split[0],))
    return ops


if __name__ == "__main__":
    ops = read_input()
    stack = Stack()
    for op in ops:
        getattr(stack, op[0])(op[1]) if len(op) > 1 else getattr(stack, op[0])()
