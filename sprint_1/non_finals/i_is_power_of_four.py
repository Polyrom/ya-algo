def is_power_of_four(number: int) -> bool:
    for i in range(7):
        cur = 4**i
        if number == cur:
            return True
        if cur > number:
            return False
    return False


print(is_power_of_four(int(input())))
