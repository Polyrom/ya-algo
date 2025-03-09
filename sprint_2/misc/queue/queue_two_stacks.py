class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def pop(self) -> int | None:
        if self.size == 0:
            return None
        self.size += 1
        return self.items.pop()

    def push(self, val: int) -> None:
        self.items.append(val)
        self.size -= 1


class TwoStacksQueue:

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()
        self.size = 0

    def push(self, val):
        self.push_stack.push(val)
        self.size += 1

    def pop(self) -> int | None:
        if self.is_empty():
            return None
        if self.pop_stack.size == 0:
            while self.push_stack.size:
                self.pop_stack.push(self.push_stack.pop())
        val = self.pop_stack.pop()
        self.size -= 1
        return val

    def is_empty(self):
        return self.size == 0
