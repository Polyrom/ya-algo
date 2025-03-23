OPENER = "("
CLOSER = ")"


def gen_brackets(n: int, openers: int = 0, closers: int = 0, brs: str = ""):
    if len(brs) == 2 * n:
        print(brs)
        return
    if openers < n:
        gen_brackets(n, openers + 1, closers, brs + OPENER)
    if closers < openers:
        gen_brackets(n, openers, closers + 1, brs + CLOSER)


n = int(input())
gen_brackets(n)
