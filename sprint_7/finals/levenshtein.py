def levenshtein(a: str, b: str) -> int:
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    n, m = len(a), len(b)

    prev = list(range(m + 1))
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        curr[0] = i

        for j in range(1, m + 1):
            insertion = prev[j] + 1
            deletion = curr[j - 1] + 1
            substitution = prev[j - 1] + (0 if a[i - 1] == b[j - 1] else 1)
            curr[j] = min(insertion, deletion, substitution)

        prev, curr = curr, prev

    return prev[m]


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    print(levenshtein(a, b))
