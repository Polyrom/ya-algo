def solution(scores: list[int]) -> bool:
    total_sum = sum(scores)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for score in scores:
        for j in range(target, score - 1, -1):
            dp[j] = dp[j] or dp[j - score]

    return dp[target]


if __name__ == "__main__":
    _ = int(input())
    game_scores = list(map(int, input().strip().split()))
    print(solution(game_scores))
