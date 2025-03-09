class Stack:
    def __init__(self):
        self.items: list[str] = []

    def size(self) -> int:
        return len(self.items)

    def push(self, value: str) -> None:
        self.items.append(value)

    def pop(self) -> str | None:
        if self.size() == 0:
            return None
        return self.items.pop()


def is_brackets_correct(seq: str) -> bool:
    closers_mapping = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = Stack()
    for br in seq:
        if br in closers_mapping:
            last_opener = stack.pop()
            if not last_opener or closers_mapping[br] != last_opener:
                return False
        else:
            stack.push(br)
    return stack.size() == 0


if __name__ == "__main__":
    bracket_seq = input()
    print(is_brackets_correct(bracket_seq))

