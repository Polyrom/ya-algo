import sys


def main():
    """
    Calculates the sum of number pairs in stdin.
    """
    num_lines = int(input())
    output_numbers = []
    for i in range(num_lines):
        line = sys.stdin.readline().rstrip()
        val1, val2 = line.split()
        result = int(val1) + int(val2)
        output_numbers.append(str(result))
    return "\n".join(output_numbers)


if __name__ == "__main__":
    print(main())
