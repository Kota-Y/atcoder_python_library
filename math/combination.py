from operator import mul
from functools import reduce

# 組み合わせ計算(nCr)
def combination(n: int, r: iny) -> int:
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under