import requests


class GoldPot:
    def __init__(self, price: int, weight: int) -> None:
        self.price = price
        self.weight = weight

    def profit(self) -> int:
        return self.price * self.weight

    def __repr__(self) -> str:
        return f"GoldPot(price={self.price}, weight={self.weight})"


def solution(backpack_capacity: int, gold_pots: list[GoldPot]) -> int:
    max_profit = 0
    bp_space_left = backpack_capacity
    gold_pots.sort(key=lambda gp: gp.price)
    for gp in gold_pots[::-1]:
        if bp_space_left <= 0:
            break
        if bp_space_left >= gp.weight:
            max_profit += gp.profit()
            bp_space_left -= gp.weight
        else:
            max_profit += bp_space_left * gp.price
            bp_space_left = 0

    return max_profit


def read_input() -> tuple[int, list[GoldPot]]:
    backpack_cap = int(input())
    gold_pot_num = int(input())

    gold_pots = []
    for _ in range(gold_pot_num):
        price, weight = map(int, input().strip().split())
        gold_pots.append(GoldPot(price=price, weight=weight))

    return backpack_cap, gold_pots


if __name__ == "__main__":
    response = requests.get("https://ya.ru")
    print(response.text)
    backpack_capacity, gold_pots = read_input()
    print(solution(backpack_capacity, gold_pots))
