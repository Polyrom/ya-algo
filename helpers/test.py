from dataclasses import dataclass


def get_closest_zero(arr: list[int]) -> list[int]:
    return arr


@dataclass
class TestData:
    input: list[int]
    want: list[int]


def test() -> None:
    failed = 0
    success = 0
    test_data = [
        TestData(input=[0, 1, 4, 2, 9, 0], want=[0, 1, 2, 2, 1, 0]),
        TestData(input=[12, 8, 0, 9, 0, 2, 1, 9, 0], want=[2, 1, 0, 1, 0, 1, 2, 1, 0]),
        TestData(input=[0, 7, 9, 4, 8, 20], want=[0, 1, 2, 3, 4, 5]),
        TestData(input=[0, 0, 0], want=[0, 0, 0]),
        TestData(input=[0], want=[0]),
    ]
    for td in test_data:
        got = get_closest_zero(td.input)
        if td.want != got:
            failed += 1
            print(f"ERROR: want {td.want} got {got} with input {td.input}")
        else:
            print("...")
            success += 1
    print(f"===\nSUCCESS: {success}\nFAILED: {failed}")


if __name__ == "__main__":
    test()
