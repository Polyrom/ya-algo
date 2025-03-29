def merge(arr, lf, mid, rg):
    result = []
    i, j = lf, mid
    while i < mid and j < rg:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    result.extend(arr[i:mid])
    result.extend(arr[j:rg])
    return result


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return arr[lf:rg]
    mid = lf + (rg - lf) // 2
    left = merge_sort(arr, lf, mid)
    right = merge_sort(arr, mid, rg)
    combined = left + right
    merged = merge(combined, 0, len(left), len(combined))
    arr[lf:rg] = merged[:]
    return merged


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
