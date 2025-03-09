class StackEffective:
    def __init__(self) -> None:
        self.max_item = None
        self.items: list[int] = []

    def size(self) -> int:
        return len(self.items)

    def pop(self) -> None:
        if self.size() == 0:
            print("error")
            return
        top = self.items.pop()
        if self.size() == 0:
            self.max_item = None
        elif top > self.max_item:
            self.max_item = 2 * self.max_item - top

    def top(self) -> None:
        if self.size() == 0:
            print("error")
            return
        top = self.items[-1]
        print(top if top < self.max_item else self.max_item)

    def push(self, value) -> None:
        if self.max_item is None:
            self.max_item = value
            self.items.append(value)
        elif value > self.max_item:
            self.items.append(value * 2 - self.max_item)
            self.max_item = value
        else:
            self.items.append(value)

    def get_max(self) -> None:
        print(self.max_item)


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
    stack = StackEffective()
    for op in ops:
        getattr(stack, op[0])(op[1]) if len(op) > 1 else getattr(stack, op[0])()
