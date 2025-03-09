class FixedSizeQueue:

    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.items = [None] * self.cap
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, val: int) -> None:
        if self.size < self.cap:
            self.items[self.tail] = val
            self.tail = (self.tail + 1) % self.cap
            self.size += 1

    def pop(self) -> int | None:
        if self.is_empty():
            return None
        x = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return x

