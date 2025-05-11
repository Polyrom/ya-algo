from collections import deque

LAND = "#"
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_island_size(sea_map: list[list[bool]], point: tuple[int, int], rows: int, cols: int) -> int:
    stack = deque([point])
    sea_map[point[0]][point[1]] = False
    size = 1

    while stack:
        x, y = stack.pop()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and sea_map[nx][ny]:
                sea_map[nx][ny] = False
                stack.append((nx, ny))
                size += 1
    return size


def find_islands(sea_map: list[list[bool]], rows: int, cols: int) -> tuple[int, int]:
    island_count = 0
    largest_island = 0

    for i in range(rows):
        for j in range(cols):
            if sea_map[i][j]:
                island_size = find_island_size(sea_map, (i, j), rows, cols)
                island_count += 1
                largest_island = max(largest_island, island_size)

    return island_count, largest_island


def read_input() -> tuple[list[list[bool]], int, int]:
    rows, cols = map(int, input().strip().split())
    sea_map = [[c == '#' for c in input().strip()] for _ in range(rows)]
    return sea_map, rows, cols


if __name__ == "__main__":
    sea_map, rows, cols = read_input()
    total, largest = find_islands(sea_map, rows, cols)
    print(total, largest)