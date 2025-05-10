"""
Вы приехали на архипелаг Алгосы (наконец-то!). Здесь есть n достопримечательностей. Ваша лодка может высадить вас
у одной из них, забрать у какой-то другой, возможно, той же самой достопримечательности и увезти на материк.
Чтобы более тщательно спланировать свой маршрут, вы хотите узнать расстояния между каждой парой достопримечательностей
Алгосов. Некоторые из них соединены мостами, по которым вы можете передвигаться в любую сторону. Всего мостов m.

Есть вероятность, что карта архипелага устроена так, что нельзя добраться от какой-то одной достопримечательности
до другой без использования лодки.

Найдите кратчайшие расстояния между всеми парами достопримечательностей.

Формат ввода
В первой строке даны числа n (1 ≤ n ≤ 100) и m (0 ≤ m ≤ n (n-1)/2). В следующих m строках описаны мосты.
Каждый мост задаётся номерами двух достопримечательностей 1 ≤ u, v ≤ n и длиной дороги 1 ≤ L ≤ 103.

Формат вывода
Выведите матрицу n × n кратчайших расстояний. На пересечении i-й строки и j-го столбца должно стоять расстояние
от i-й до j-й достопримечательности. Если между какой-то парой нет пути, то в соответствующей клетке поставьте -1.
"""

import math

GraphAssocWeighted = dict[int, dict[int, int]]


def find_closest_neighbor(distance: dict[int, int], visited: set[int]) -> int | None:
    shortest_distance = math.inf
    closest_neighbor = None
    for v, dist in distance.items():
        if dist < shortest_distance and v not in visited:
            shortest_distance = dist
            closest_neighbor = v
    return closest_neighbor


def find_paths(graph: GraphAssocWeighted, start: int) -> list[int]:
    visited = set()
    distance = dict.fromkeys(graph, math.inf)
    distance[start] = 0
    for v, d in graph[start].items():
        if d < distance[v]:
            distance[v] = d

    closest_neighbor = find_closest_neighbor(distance, visited)
    while closest_neighbor is not None:
        dist = distance[closest_neighbor]
        neighbors = graph[closest_neighbor]
        for n, d in neighbors.items():
            new_dist = dist + d
            if distance[n] > new_dist:
                distance[n] = new_dist
        visited.add(closest_neighbor)
        closest_neighbor = find_closest_neighbor(distance, visited)
    return [d if d != math.inf else -1 for d in distance.values()]


def find_all_paths(graph: GraphAssocWeighted) -> list[list[int]]:
    all_paths = []
    for v in graph:
        all_paths.append(find_paths(graph, v))
    return all_paths


def read_input() -> GraphAssocWeighted:
    vertices_num, edges_num = tuple(map(int, input().strip().split()))
    assoc_list: GraphAssocWeighted = {v: {} for v in range(1, vertices_num + 1)}
    for _ in range(edges_num):
        from_, to, weight = tuple(map(int, input().strip().split()))
        if to not in assoc_list[from_] or assoc_list[from_][to] > weight:
            assoc_list[from_][to] = weight
            assoc_list[to][from_] = weight
    return assoc_list


if __name__ == "__main__":
    adjacents = read_input()
    paths = find_all_paths(adjacents)
    for p in paths:
        print(" ".join(map(str, p)))
