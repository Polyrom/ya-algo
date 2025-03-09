from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    num_days = len(temperatures)
    if num_days == 1:
        return 1

    chaotic_days = 0
    for i in range(num_days):
        is_day_before_colder = is_day_after_colder = True
        if i > 0:
            is_day_before_colder = temperatures[i] > temperatures[i - 1]
        if i <= num_days - 2:
            is_day_after_colder = temperatures[i] > temperatures[i + 1]
        if is_day_before_colder and is_day_after_colder:
            chaotic_days += 1
    return chaotic_days


def read_input() -> List[int]:
    _ = int(input())
    return list(map(int, input().strip().split()))


temperatures = read_input()
print(get_weather_randomness(temperatures))
