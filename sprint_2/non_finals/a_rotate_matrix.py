Matrix = list[list[str]]


def rotate(matrix: Matrix, rows: int, cols: int) -> Matrix:
    rotated = []
    for i in range(cols):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        rotated.append(new_row)
    return rotated


def read_input() -> tuple[int, int, Matrix]:
    rows = input()
    cols = input()
    matrix: list[str] = []
    for _ in range(int(rows)):
        vals = input()
        matrix.append(list(vals.split()))
    return int(rows), int(cols), matrix


def print_matrix(matrix: Matrix) -> None:
    for row in matrix:
        print(" ".join(row))


if __name__ == "__main__":
    rows, cols, matrix = read_input()
    print_matrix(rotate(matrix, rows, cols))
