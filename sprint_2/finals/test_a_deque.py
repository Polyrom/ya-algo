from a_deque import run_deque


def read_test_data(path: str):
    with open(path) as f:
        cap = f.readline()
        ops = []
        for line in f:
            op_split = line.strip().split()
            if len(op_split) > 1:
                ops.append((op_split[0], int(op_split[1])))
            else:
                ops.append((op_split[0], None))
    return int(cap), ops


def read_expected_data(path: str):
    with open(path) as f:
        results = []
        for line in f:
            results.append(line.strip())
        return results


def test_deque():
    cap, ops = read_test_data("test_data.txt")
    expected = read_expected_data("expected.txt")
    actual = run_deque(cap, ops)
    assert expected == actual
