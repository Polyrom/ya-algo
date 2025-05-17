"""
Дано количество учебных занятий, проходящих в одной аудитории. Для каждого из них указано время начала и конца.
Нужно составить расписание, в соответствии с которым в классе можно будет провести как можно больше занятий.

Если возможно несколько оптимальных вариантов, то выведите любой.
Возможно одновременное проведение более чем одного занятия нулевой длительности.

Формат ввода
В первой строке задано число занятий. Оно не превосходит 1000. Далее для каждого занятия в отдельной строке записано
время начала и конца, разделённые пробелом. Время задаётся одним целым числом h, если урок начинается/заканчивается
ровно в h часов. Если же урок начинается/заканчивается в h часов m минут, то время записывается как h.m.
Гарантируется, что каждое занятие начинается не позже, чем заканчивается. Указываются только значащие цифры.

Формат вывода
Выведите в первой строке наибольшее число уроков, которое можно провести в аудитории.
Далее выведите время начала и конца каждого урока в отдельной строке в порядке их проведения.
"""

from collections import namedtuple

TimeSlot = namedtuple("TimeSlot", "start end")


def solution(times: list[TimeSlot]) -> list[TimeSlot]:
    sorted_times = sorted(times, key=lambda x: (x.end, x.start))
    if not sorted_times:
        return []

    optimals = [sorted_times[0]]
    last_end_time = sorted_times[0].end

    for time_slot in sorted_times[1:]:
        if time_slot.start >= last_end_time:
            optimals.append(time_slot)
            last_end_time = time_slot.end

    return optimals


def read_input() -> list[TimeSlot]:
    events = int(input())
    times = []
    for _ in range(events):
        time = tuple(map(float, input().strip().split()))
        times.append(TimeSlot(start=time[0], end=time[1]))
    return times


if __name__ == "__main__":
    times = read_input()
    optimal = solution(times)
    print(len(optimal))
    for ts in optimal:
        start = int(ts.start) if ts.start.is_integer() else ts.start
        end = int(ts.end) if ts.end.is_integer() else ts.end
        print(start, end)
