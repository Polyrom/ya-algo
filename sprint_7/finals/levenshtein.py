def levenshtein(a: str, b: str) -> int:
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(0, n + 1):
        dp[i][0] = i
    for i in range(0, m + 1):
        dp[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = dp[i - 1][j] + 1
            deletion = dp[i][j - 1] + 1
            substitution = dp[i - 1][j - 1] + (1 if a[i - 1] != b[j - 1] else 0)
            dp[i][j] = min(insertion, deletion, substitution)

    return dp[n][m]


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    print(levenshtein(a, b))
