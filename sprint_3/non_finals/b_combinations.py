BUTTONS = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


def gen_combos(digits: list[int], combo: str = ""):
    if not digits:
        return [combo]

    current_digit = digits[0]
    letters = BUTTONS.get(current_digit, "")

    combinations = []

    for letter in letters:
        combinations.extend(gen_combos(digits[1:], combo + letter))

    return combinations


digits = list(map(int, list(input().strip())))
print(" ".join(gen_combos(digits)))
