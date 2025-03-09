from typing import List, Tuple


class Coordinate:
    def __init__(self, a: int, b: int) -> None:
        self.row = a
        self.col = b

    def is_out_of_bounds(self, max_row: int, max_col: int) -> bool:
        return self.row < 0 or self.row > max_row or self.col > max_col or self.col < 0

    def get_neighbours_coordinates(self) -> List["Coordinate"]:
        return [
            Coordinate(self.row - 1, self.col),
            Coordinate(self.row + 1, self.col),
            Coordinate(self.row, self.col - 1),
            Coordinate(self.row, self.col + 1),
        ]


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    target = Coordinate(row, col)
    neighbours_coordinates = target.get_neighbours_coordinates()
    neighbours = []
    for coord in neighbours_coordinates:
        if not coord.is_out_of_bounds(len(matrix) - 1, len(matrix[0]) - 1):
            neighbours.append(matrix[coord.row][coord.col])
    return sorted(neighbours)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    _ = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
