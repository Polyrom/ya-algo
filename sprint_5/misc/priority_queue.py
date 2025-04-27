class MinHeap:
    FIRST_ELEMENT_IDX = 1

    def __init__(self, values: list[int]) -> None:
        self.values: list[int | None] = [None]
        if len(values) > 0:
            self.values.append(values[0])
        for val in values[1:]:
            self.add(val)

    def add(self, key: int) -> None:
        self.values.append(key)
        self._sift_up(key, len(self.values) - 1)

    def pop_min(self) -> int | None:
        if len(self.values) < 2:
            return None
        result = self.values[self.FIRST_ELEMENT_IDX]
        self.values[self.FIRST_ELEMENT_IDX] = self.values.pop()
        self._sift_down(self.FIRST_ELEMENT_IDX)
        return result

    def _sift_up(self, key: int, index: int) -> None:
        if index == self.FIRST_ELEMENT_IDX:
            return

        parent_index = index // 2
        if self.values[index] < self.values[parent_index]:  # type: ignore (replace with > for MaxHeap)
            self.values[parent_index], self.values[index] = self.values[index], self.values[parent_index]
            self._sift_up(key, parent_index)

    def _sift_down(self, index: int) -> None:
        left_index = index * 2
        right_index = left_index + 1
        max_index = len(self.values) - 1

        if left_index > max_index:
            return
        if right_index <= max_index and (self.values[right_index] < self.values[left_index]):  # type: ignore
            max_index = right_index
        else:
            max_index = left_index

        if self.values[max_index] < self.values[index]:  # type: ignore
            self.values[max_index], self.values[index] = self.values[index], self.values[max_index]
            self._sift_down(max_index)


def test():
    """
        -1
       /   \
      4     12
     / \'   /
    9   8 49
    """
    bh = MinHeap([4, 9, 12, 8, -1, 49])
    assert bh.values == [None, -1, 4, 12, 9, 8, 49], f"actual: {bh.values}"

    popped = bh.pop_min()
    assert popped == -1, f"actual: {popped}"
    popped = bh.pop_min()
    assert popped == 4, f"actual: {popped}"
    assert bh.values == [None, 8, 9, 12, 49], f"actual: {bh.values}"


if __name__ == "__main__":
    test()
